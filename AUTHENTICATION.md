# Authentication System - Quick Reference

## User Modes

### Guest Mode (Non-Persistent)
- No account needed
- Click "Continue as Guest" in auth modal
- Session cleared on page reload
- Perfect for testing
- Command history only in-memory

### Registered Mode (Persistent)
- Create account or login
- Session saved to database
- Access account management
- Command history persists across sessions
- Lasts 30 days without activity

---

## Registration Process

1. Click "Login / Register" button (top-right)
2. Click "Don't have an account? Register"
3. Enter username (3+ characters)
4. Enter password (6+ characters)
5. Confirm password
6. Click "Register"
7. Automatically logged in

### Password Requirements
- Minimum 6 characters
- Hashed with Argon2id + salt
- Auto-strengthened against brute force

---

## Account Management

### Login
1. Click "Login / Register"
2. Enter username and password
3. Click "Login"
4. Session restored automatically

### Change Password
1. Click "Account" (only visible when logged in)
2. Enter current password
3. Enter new password (6+ chars)
4. Confirm new password
5. Click "Change Password"

### Delete Account
1. Click "Account"
2. Scroll to "Danger Zone"
3. Enter your password
4. Click "Delete Account"
5. Confirm when prompted
6. Account and all data permanently deleted

### Logout
1. Click "Logout" button (only visible when logged in)
2. Returns to guest mode
3. Previous session saved

---

## Session Persistence

### For Registered Users
Automatically saved:
- ✅ Command history
- ✅ File system state (created files/directories)
- ✅ Environment variables
- ✅ Current working directory
- ✅ Terminal position

Saved automatically when:
- Command is executed
- History is cleared
- Page is left/closed

Load automatically when:
- You login
- Page reloads while logged in

### For Guest Users
NOT saved:
- ✅ Commands cleared on reload
- ✅ Files deleted on reload
- ✅ Environment variables reset
- ✅ Perfect for trying without commitment

---

## Database Info

**Users Database: `users.db`** (SQLite)

### Users Table
- Username (unique, indexed)
- Password hash (Argon2id with salt)
- Created timestamp
- Last login timestamp

### Session Data Table  
- Per-user session state
- Terminal state (JSON)
- Command history (JSON array)
- File system (JSON tree)
- Environment variables (JSON)
- Update timestamp

---

## Security Details

### Argon2id Hashing
- **Algorithm**: Argon2id
- **Iterations**: 2 time-cost
- **Memory**: 64MB per hash
- **Parallelism**: 4 threads
- **Salt**: Automatic per password

Protection against:
- ✅ Dictionary attacks (memory-hard)
- ✅ GPU/ASIC attacks (sequential memory)
- ✅ Rainbow tables (unique salts)
- ✅ Brute force (time-cost)

### Session Security
- HTTP-only cookies (XSS protection)
- 30-day expiration (registered)
- Browser-only (guest mode)
- Automatic on logout

---

## API Endpoints Reference

### Authentication
```
POST   /api/auth/register        - Register new account
POST   /api/auth/login           - Login with credentials
POST   /api/auth/login-guest     - Start guest session
POST   /api/auth/logout          - Logout (clears session)
GET    /api/auth/status          - Check login status
POST   /api/auth/change-password - Change user password
DELETE /api/auth/delete-account  - Delete account + data
```

### Session Management
```
GET    /api/session/load         - Load saved session (registered only)
POST   /api/session/save         - Save session (registered only)
```

---

## Configuration

### Production Setup

Set environment variables:
```bash
export SECRET_KEY="your-long-random-secret-key"
export FLASK_ENV="production"
export SQLALCHEMY_DATABASE_URI="sqlite:///users.db"
```

Or create `.env` file:
```
SECRET_KEY=your-secret-key
FLASK_ENV=production
SQLALCHEMY_DATABASE_URI=sqlite:///users.db
```

### Customize Argon2 Parameters

Edit `app.py`:
```python
ph = PasswordHasher(
    time_cost=2,        # Increase for slower hashing
    memory_cost=65536,  # Increase for more memory
    parallelism=4,      # Adjust based on CPU cores
)
```

---

## Troubleshooting

### "Failed to register" Error
- Username must be 3+ characters
- Password must be 6+ characters  
- Username might be taken (try different one)

### "Invalid username or password"
- Check caps lock
- Verify correct username/password
- Passwords are case-sensitive

### Session not saving
- Ensure you're logged in (check top-right)
- Execute at least one command to trigger save
- Check browser console for errors

### Lost session data
- Session lasts 30 days without login
- If longer, manually re-login
- Logout doesn't delete session, just logs out

### Delete account not working
- Must enter correct password
- Confirm account deletion when prompted
- All data permanently deleted (irreversible)

---

## Examples

### Register and Use
```bash
# 1. Click "Login / Register" → "Register"
# 2. Username: alice
# 3. Password: SecurePass123
# 4. Logged in automatically

# Now use terminal - everything saved:
$ mkdir my_project
$ echo "test" > my_project/file.txt
$ cd my_project
$ pwd
/home/alice/my_project

# Close browser, come back later
# Login with same credentials
# Everything restored!
```

### Change Password
```bash
# 1. Click "Account" button
# 2. Current Password: SecurePass123
# 3. New Password: NewPass456
# 4. Confirm: NewPass456
# 5. Click "Change Password"

# Next login use: NewPass456
```

### Delete Account
```bash
# 1. Click "Account"
# 2. Scroll to "Danger Zone"
# 3. Password: CurrentPassword
# 4. Click "Delete Account"
# 5. Confirm: Yes, delete
# Account and all data gone forever
```

---

## File Structure

```
BrowserLinux/
├── app.py                      # Flask backend with auth
├── requirements.txt            # Python dependencies  
├── users.db                    # SQLite database (auto-created)
├── templates/
│   └── terminal_simple.html    # Frontend with auth UI
├── README.md                   # Main documentation
└── SESSION_MANAGEMENT.md       # Session details
```

---

## What's New in v2.3

✅ **User Registration System**
- Create accounts with secure password hashing
- Username/password validation
- Duplicate username detection

✅ **Argon2id Password Security**
- Industry-standard algorithm
- Automatic salt per password
- Time/memory/parallelism cost
- Resistant to GPU attacks

✅ **Session Persistence**
- Database-backed session storage
- 30-day expiration
- Auto-save on command execution
- Auto-restore on login

✅ **Account Management**
- Change password with verification
- Delete account and all data
- Login/logout functionality

✅ **Guest Mode**
- Non-persistent browser sessions
- No account creation needed
- Perfect for testing

✅ **Authentication UI**
- Modal-based login/register
- Account settings panel
- User display in top bar
- Mode indicator (guest/registered)

---

## Next Steps

1. **Run the app**: `python app.py`
2. **Open browser**: http://localhost:5000
3. **Choose mode**:
   - Guest: Click "Continue as Guest"
   - Register: Click "Register"
4. **Try commands**: `ls`, `mkdir`, `cd`, etc.
5. **Close/reopen browser**:
   - Guests: Everything cleared ❌
   - Registered: Everything restored ✅
