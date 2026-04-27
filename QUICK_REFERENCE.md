# Quick Reference: Available Commands

## 📂 File & Directory Operations

| Command | Usage | Example |
|---------|-------|---------|
| `ls` | List files | `ls -la` |
| `cd` | Change directory | `cd /home/user` |
| `pwd` | Print working directory | `pwd` |
| `mkdir` | Create directory | `mkdir newdir` |
| `rmdir` | Remove empty dir | `rmdir olddir` |
| `touch` | Create file | `touch file.txt` |
| `cp` | Copy file | `cp src.txt dst.txt` |
| `mv` | Move/rename | `mv old.txt new.txt` |
| `rm` | Delete file | `rm file.txt` |
| `find` | Search files | `find . pattern` |

## 📄 File Viewing & Searching

| Command | Usage | Example |
|---------|-------|---------|
| `cat` | Display file | `cat file.txt` |
| `head` | First N lines | `head -n 5 file.txt` |
| `tail` | Last N lines | `tail -n 10 file.txt` |
| `grep` | Search text | `grep hello file.txt` |

## 🖥️ System Information

| Command | Usage | Example |
|---------|-------|---------|
| `date` | Show date/time | `date` |
| `cal` | Show calendar | `cal` |
| `whoami` | Show username | `whoami` |
| `hostname` | Show hostname | `hostname` |
| `uptime` | Session uptime | `uptime` |
| `df` | Disk usage | `df` |
| `du` | Directory size | `du -s .` |
| `free` | Memory stats | `free` |
| `chmod` | Change permissions | `chmod 755 file.txt` |
| `chown` | Change owner | `chown user file.txt` |

## 🔧 Environment & Variables

| Command | Usage | Example |
|---------|-------|---------|
| `echo` | Print text | `echo "Hello $USER"` |
| `export` | Set variable | `export VAR=value` |
| `env` | Show all variables | `env` |
| `unset` | Delete variable | `unset VAR` |

## 💡 Terminal Controls & Help

| Command | Usage | Example |
|---------|-------|---------|
| `clear` | Clear screen | `clear` |
| `history` | Show history | `history` |
| `help` | Show commands | `help` |
| `sudo` | "Elevated" access | `sudo whoami` |

---

## 🎯 Common Tasks

### Create & Edit Files
```bash
touch myfile.txt
echo "content" > myfile.txt
cat myfile.txt
```

### Navigate Directories
```bash
pwd                    # Where am I?
ls                     # What's here?
mkdir folder          # Create folder
cd folder             # Go into folder
cd ..                 # Go back
cd ~                  # Go home
```

### Manage Files
```bash
cp file.txt backup.txt    # Backup
mv file.txt renamed.txt   # Rename
rm unwanted.txt           # Delete
find . .txt               # Search
```

### View File Content
```bash
cat bigfile.txt        # All content
head -n 20 bigfile.txt # First 20 lines
tail -n 20 bigfile.txt # Last 20 lines
grep "pattern" file.txt # Search lines
```

### System Info
```bash
whoami                 # Current user
hostname              # Computer name
date                  # Current time
uptime               # How long running
df                   # Disk space
free                 # Memory usage
```

### Environment
```bash
echo $USER            # Print variable
export MY_VAR=123     # Set variable
env                   # Show all variables
```

---

## ⌨️ Keyboard Shortcuts

| Key | Function |
|-----|----------|
| ↑ / ↓ | Previous/Next command |
| Tab | Auto-complete filename |
| Ctrl+A | Start of line |
| Ctrl+E | End of line |
| Ctrl+C | Cancel command |
| Ctrl+L | Clear screen |
| Home | Start of line |
| End | End of line |

---

## 📝 Output Redirection

| Operator | Usage | Example |
|----------|-------|---------|
| `>` | Write to file | `echo hello > file.txt` |
| `>>` | Append to file | `echo world >> file.txt` |

```bash
ls > myfiles.txt        # Save list to file
echo "more" >> myfiles.txt # Add to file
cat myfiles.txt         # View saved list
```

---

## 🚀 Tips & Tricks

### Use Variables
```bash
export NAME=John
echo Hello $NAME        # Hello John
```

### Command History
```bash
history                 # See all previous commands
↑ key                   # Replay last command
↑↑ key                  # Go back further
```

### Combine Commands
```bash
mkdir mydir && cd mydir        # Create AND enter
cat file.txt | grep pattern    # (Coming soon)
```

### Navigation Shortcuts
```bash
cd ~                    # Home directory
cd -                    # Previous directory
cd ..                   # Parent directory
pwd                     # Print current path
```

---

## 🔍 Examples by Task

### Task: Create a project directory structure
```bash
mkdir myproject
cd myproject
mkdir src
mkdir docs
touch README.txt
ls -la
```

### Task: Backup files
```bash
cp important.txt important_backup.txt
ls
```

### Task: Find files
```bash
find . .txt            # Find all .txt files
find . config          # Find files with "config"
```

### Task: Check disk usage
```bash
df                     # Total usage
du -s .                # Current folder size
```

### Task: View file contents
```bash
cat README.txt
head -n 5 README.txt   # First 5 lines
tail -n 3 README.txt   # Last 3 lines
```

---

## ✅ What's Implemented (34 commands)

✓ File operations: ls, cd, pwd, mkdir, rmdir, touch, cp, mv, rm, find  
✓ File viewing: cat, head, tail, grep  
✓ System info: date, cal, whoami, hostname, uptime, df, du, free  
✓ Permissions: chmod, chown  
✓ Environment: echo, export, env, unset, history, help  
✓ Terminal: clear, sudo (joke)  

---

## 🔜 Coming Soon

- **Text processing**: sed, awk, sort, cut, wc, uniq
- **Archives**: tar, gzip, zip
- **Process**: ps, top, kill, sleep
- **Network**: curl, wget, ping
- **Editors**: nano, vim (complex but fun!)

---

## ❓ Need Help?

Type `help` in the terminal to see the command list!

For detailed documentation, see:
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) - For developers
- [INTEGRATION_STATUS.md](INTEGRATION_STATUS.md) - Full command status
- [COMMAND_MAPPING.md](COMMAND_MAPPING.md) - Implementation details

---

**Last Updated**: April 27, 2026  
**Status**: 34/65 commands implemented (52%)
