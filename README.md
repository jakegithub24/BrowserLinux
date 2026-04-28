# Linux Terminal Simulator with User Authentication

A web-based Linux terminal emulator with user registration, authentication, and session management. Features include guest mode for non-persistent sessions and registered user mode with full session persistence.

## Features

### Authentication & User Management
- **User Registration**: Create accounts with username (3+ chars) and password (6+ chars)
- **Secure Login**: Password verification using Argon2id hashing with salt
- **Guest Mode**: Use as guest without creating an account (non-persistent session)
- **Account Management**:
  - Change password (requires current password verification)
  - Delete account (requires password confirmation, removes all user data)
  - Persistent session history for registered users

### Session Management
- **Registered Users**: 
  - Full session persistence (command history, file system state, environment variables)
  - Sessions expire after 30 days of inactivity
  - Automatic session restoration on login
  
- **Guest Users**: 
  - Non-persistent sessions (cleared on page reload)
  - Perfect for quick testing without account creation

### Terminal Features
- **Virtual File System**: Complete in-memory Linux filesystem with full path support
- **Command Support** (30+ commands):
  - File operations: `ls`, `cd`, `pwd`, `mkdir`, `touch`, `rm`, `cat`, `cp`, `mv`, `find`, `head`, `tail`
  - System info: `whoami`, `hostname`, `uptime`, `date`, `df`, `du`, `free`
  - Shell utilities: `echo`, `grep`, `history`, `clear`, `env`, `export`, `unset`
  - And more...
- **Output Redirection**: Redirect command output to files using `>`
- **Command History**: Access previous commands from sidebar or `history` command
- **Environment Variables**: Full environment variable support with `export` and `unset`

## Installation & Setup

### Prerequisites
- Python 3.8+
- Flask and dependencies (see requirements.txt)

### Quick Start

1. **Clone/extract the repository**
```bash
cd /path/to/BrowserLinux
```

2. **Create and activate virtual environment**
```bash
python3 -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

The app will start on `http://localhost:5000`

## Usage

### First Time Users

1. Open http://localhost:5000 in your browser
2. Click "Login / Register" or "Continue as Guest"
3. For guest mode: Session will be cleared on page reload
4. To create an account:
   - Click "Register"
   - Enter username (3+ characters)
   - Enter password (6+ characters)
   - Confirm password
   - Submit

### Registered Users

After logging in:
- Your terminal session is automatically saved
- File system state persists across sessions
- Command history is preserved
- Access "Account" button to:
  - Change your password
  - Delete your account

### Terminal Examples

```bash
# Navigate filesystem
cd Documents
pwd

# Create files
touch myfile.txt
echo "Hello World" > greeting.txt

# View files
cat greeting.txt
ls -l

# File operations
mkdir projects
cp greeting.txt greeting_backup.txt
mv greeting_backup.txt projects/

# System information
whoami
hostname
uptime
date

# Search
grep "pattern" myfile.txt

# Environment
export MY_VAR="value"
echo $MY_VAR
```

## Architecture

### Backend (Flask)

**API Endpoints:**

Authentication:
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/login-guest` - Start guest session
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/status` - Check auth status
- `POST /api/auth/change-password` - Change password
- `DELETE /api/auth/delete-account` - Delete account

Session Management:
- `POST /api/session/save` - Save terminal state (registered users only)
- `GET /api/session/load` - Load terminal state (registered users only)

**Database:**
- SQLite with two main tables:
  - `users`: Username and password hash (Argon2id)
  - `session_data`: Terminal state, file system, history, environment vars (JSON)

### Frontend (HTML/JavaScript)

**Key Components:**
- Virtual File System class: In-memory Linux filesystem implementation
- Environment class: Manages environment variables
- Command parser and executor
- Authentication modal system
- Session auto-save on command execution

## Security

### Password Security
- **Argon2id**: Industry-standard password hashing algorithm with:
  - Automatic salt generation per password
  - Time/memory cost parameters to resist brute-force attacks
  - Protection against GPU/ASIC attacks

### Session Security
- Flask session cookies with:
  - HttpOnly flag (prevents XSS access)
  - Secure flag for HTTPS (in production)
  - 30-day expiration for registered users
  - No expiration for guest sessions (browser-based only)

### Data Protection
- User passwords never stored in plaintext
- Session data encrypted in transit (use HTTPS in production)
- Account deletion removes all associated data

## Configuration

### Environment Variables

Create a `.env` file for production:

```bash
# Flask secret key (generate one for production!)
export SECRET_KEY="your-secret-key-here"

# Database URI (default: SQLite)
export SQLALCHEMY_DATABASE_URI="sqlite:///users.db"

# Flask environment
export FLASK_ENV="production"
```

### Argon2id Parameters

Customize password hashing in `app.py`:
```python
from argon2 import PasswordHasher

ph = PasswordHasher(
    time_cost=2,        # Number of iterations
    memory_cost=65536,  # Memory in KB
    parallelism=4,      # Number of parallel threads
)
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT NOW,
    last_login DATETIME
)
```

### Session Data Table
```sql
CREATE TABLE session_data (
    id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE FOREIGN KEY,
    terminal_state TEXT,      -- JSON: {cwd, previousCwd}
    command_history TEXT,     -- JSON array
    file_system TEXT,         -- JSON tree structure
    environment_vars TEXT,    -- JSON object
    created_at DATETIME,
    updated_at DATETIME
)
```

## Troubleshooting

### Database Issues
- Delete `users.db` to reset database
- Database recreated automatically on app start

### Session Not Saving
- Ensure you're logged in (check top-right)
- Check browser console for network errors
- Verify Flask app is running and accessible

### Argon2 Installation Issues

On Linux:
```bash
pip install --upgrade pip
pip install argon2-cffi
```

On macOS:
```bash
brew install libffi
pip install argon2-cffi
```

## Future Enhancements

- [ ] Two-factor authentication (2FA)
- [ ] OAuth/Social login integration
- [ ] File upload/download capability
- [ ] Terminal themes and customization
- [ ] Multi-user collaboration features
- [ ] Command history search
- [ ] Keyboard shortcuts
- [ ] Terminal session sharing

## License

MIT License - Feel free to use and modify

## Contributing

Contributions welcome! Areas of improvement:
- Additional shell commands
- Better terminal styling
- Performance optimizations
- Security audits
- Documentation

## Changelog

### v2.3 (Current)
- ✅ Added Argon2id password hashing with salt
- ✅ Implemented user registration system
- ✅ Added account management (change password, delete account)
- ✅ Session persistence for registered users
- ✅ Non-persistent guest mode
- ✅ Authentication UI with modals

### v2.2
- Non-persistent session implementation

### v2.1
- Basic terminal commands
- Virtual file system

### v2.0
- Initial Flask backend
- Basic UI

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review browser console for errors
3. Check Flask server logs
4. Verify all dependencies are installed correctly
