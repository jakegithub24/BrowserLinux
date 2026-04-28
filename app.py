from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError
import json
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 86400 * 30  # 30 days

# Initialize extensions
db = SQLAlchemy(app)
Session(app)
ph = PasswordHasher()

# ===================== DATABASE MODELS =====================
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return f'<User {self.username}>'

class SessionData(db.Model):
    __tablename__ = 'session_data'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    terminal_state = db.Column(db.Text, nullable=False)  # JSON serialized
    command_history = db.Column(db.Text, nullable=False)  # JSON array
    file_system = db.Column(db.Text, nullable=False)  # JSON serialized
    environment_vars = db.Column(db.Text, nullable=False)  # JSON object
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<SessionData user_id={self.user_id}>'

# ===================== HELPER FUNCTIONS =====================
def hash_password(password):
    """Hash password using Argon2id"""
    return ph.hash(password)

def verify_password(password, password_hash):
    """Verify password against hash"""
    try:
        ph.verify(password_hash, password)
        return True
    except (VerifyMismatchError, VerificationError):
        return False

# ===================== API ROUTES =====================
@app.route('/')
def index():
    return render_template('terminal_simple.html')

@app.route('/api/auth/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '')

    # Validation
    if not username or len(username) < 3:
        return jsonify({'error': 'Username must be at least 3 characters'}), 400
    if not password or len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400

    # Check if user exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    try:
        # Create new user
        new_user = User(
            username=username,
            password_hash=hash_password(password)
        )
        db.session.add(new_user)
        db.session.commit()

        # Create initial session data
        initial_session = SessionData(
            user_id=new_user.id,
            terminal_state=json.dumps({'cwd': '/home/user', 'previousCwd': '/home/user'}),
            command_history=json.dumps([]),
            file_system=json.dumps({}),
            environment_vars=json.dumps({
                'HOME': '/home/user',
                'USER': username,
                'HOSTNAME': 'linux-emulator',
                'PATH': '/usr/local/bin:/usr/bin:/bin',
                'SHELL': '/bin/bash',
                'PWD': '/home/user'
            })
        )
        db.session.add(initial_session)
        db.session.commit()

        return jsonify({'message': 'Registration successful'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '')

    user = User.query.filter_by(username=username).first()
    if not user or not verify_password(password, user.password_hash):
        return jsonify({'error': 'Invalid username or password'}), 401

    try:
        # Update last login
        user.last_login = datetime.utcnow()
        db.session.commit()

        # Set session
        session.permanent = True
        session['user_id'] = user.id
        session['username'] = user.username
        session['mode'] = 'registered'

        return jsonify({
            'message': 'Login successful',
            'username': user.username,
            'user_id': user.id
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login-guest', methods=['POST'])
def login_guest():
    """Start guest session (non-persistent)"""
    session.permanent = False
    session['mode'] = 'guest'
    session['username'] = 'guest'
    
    return jsonify({
        'message': 'Guest mode activated',
        'username': 'guest',
        'mode': 'guest'
    }), 200

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """Logout user"""
    session.clear()
    return jsonify({'message': 'Logged out'}), 200

@app.route('/api/auth/status', methods=['GET'])
def auth_status():
    """Get current auth status"""
    if 'user_id' in session:
        user = User.query.get(session.get('user_id'))
        if user:
            return jsonify({
                'authenticated': True,
                'username': user.username,
                'user_id': user.id,
                'mode': 'registered'
            }), 200

    return jsonify({
        'authenticated': False,
        'mode': 'guest'
    }), 200

@app.route('/api/auth/change-password', methods=['POST'])
def change_password():
    """Change password for logged-in user"""
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401

    data = request.get_json()
    old_password = data.get('old_password', '')
    new_password = data.get('new_password', '')

    if not new_password or len(new_password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400

    user = User.query.get(session['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if not verify_password(old_password, user.password_hash):
        return jsonify({'error': 'Incorrect current password'}), 401

    try:
        user.password_hash = hash_password(new_password)
        db.session.commit()
        return jsonify({'message': 'Password changed successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/delete-account', methods=['DELETE'])
def delete_account():
    """Delete user account and associated data"""
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401

    data = request.get_json()
    password = data.get('password', '')

    user = User.query.get(session['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if not verify_password(password, user.password_hash):
        return jsonify({'error': 'Incorrect password'}), 401

    try:
        # Delete session data
        SessionData.query.filter_by(user_id=user.id).delete()
        # Delete user
        db.session.delete(user)
        db.session.commit()

        # Clear session
        session.clear()

        return jsonify({'message': 'Account deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/session/save', methods=['POST'])
def save_session():
    """Save terminal session state for registered users"""
    if 'user_id' not in session:
        # Guest mode - no persistence
        return jsonify({'message': 'Guest mode - no persistence'}), 200

    data = request.get_json()
    user_id = session['user_id']

    try:
        session_data = SessionData.query.filter_by(user_id=user_id).first()
        if not session_data:
            session_data = SessionData(
                user_id=user_id,
                terminal_state=json.dumps({}),
                command_history=json.dumps([]),
                file_system=json.dumps({}),
                environment_vars=json.dumps({})
            )
            db.session.add(session_data)

        session_data.terminal_state = json.dumps(data.get('terminal_state', {}))
        session_data.command_history = json.dumps(data.get('command_history', []))
        session_data.file_system = json.dumps(data.get('file_system', {}))
        session_data.environment_vars = json.dumps(data.get('environment_vars', {}))
        session_data.updated_at = datetime.utcnow()

        db.session.commit()
        return jsonify({'message': 'Session saved'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/session/load', methods=['GET'])
def load_session():
    """Load terminal session state for registered users"""
    if 'user_id' not in session:
        # Guest mode - no persistence
        return jsonify({'data': None, 'mode': 'guest'}), 200

    user_id = session['user_id']
    session_data = SessionData.query.filter_by(user_id=user_id).first()

    if not session_data:
        return jsonify({'data': None, 'mode': 'registered'}), 200

    try:
        return jsonify({
            'data': {
                'terminal_state': json.loads(session_data.terminal_state),
                'command_history': json.loads(session_data.command_history),
                'file_system': json.loads(session_data.file_system),
                'environment_vars': json.loads(session_data.environment_vars)
            },
            'mode': 'registered'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
