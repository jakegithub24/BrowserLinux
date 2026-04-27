# Developer Guide: Browser Terminal Implementation

## Quick Reference - Command Categories

### 📁 File Operations (✅ 9/9 implemented)
- **Navigation**: `ls`, `cd`, `pwd`
- **Creation**: `mkdir`, `touch`
- **Deletion**: `rm`, `rmdir`
- **Copying**: `cp`, `mv`
- **Search**: `find`
- **File viewing**: `cat`, `head`, `tail`

### 📝 Text Processing (⚠️ 1/6 implemented)
- **Implemented**: `grep`
- **To implement**: `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`

### 📊 System Info (✅ 8/8 implemented)
- **User/Host**: `whoami`, `hostname`
- **Time**: `date`, `cal`, `uptime`
- **Resources**: `df`, `du`, `free`
- **Permissions**: `chmod`, `chown`

### 🛠️ Environment (✅ 5/5 implemented)
- `export` - Set variables
- `unset` - Remove variables
- `env` - Show all variables
- `echo` - Print text
- History/Help: `history`, `help`

### 🔧 Easy Next Steps (Ready to implement)

#### 1. Text Processing Tools
Add these after `grep` implementation. Use JavaScript string methods:

```javascript
function sortCmd(args, fs) {
    const files = args.filter(a => !a.startsWith('-'));
    let content = '';
    for (const f of files) {
        const c = fs.readFile(f);
        if (c) content += c;
    }
    return content.split('\n').sort().join('\n');
}

function wcCmd(args, fs) {
    const files = args.filter(a => !a.startsWith('-'));
    let lines = 0, words = 0, bytes = 0;
    for (const f of files) {
        const c = fs.readFile(f);
        if (c) {
            lines += c.split('\n').length;
            words += c.split(/\s+/).length;
            bytes += c.length;
        }
    }
    return `${lines} ${words} ${bytes}`;
}
```

#### 2. Archive/Compression
Install via CDN or npm and wrap:

```javascript
// Uses external library (add to <head>):
// <script src="https://cdn.jsdelivr.net/npm/pako/dist/pako.js"></script>

function gzipCmd(args, fs) {
    const file = args[0];
    const content = fs.readFile(file);
    if (!content) return `\x1b[31mgzip: ${file}: No such file\x1b[0m`;
    
    const compressed = pako.gzip(content);
    const base64 = btoa(String.fromCharCode(...compressed));
    fs.writeFile(file + '.gz', base64);
    return '';
}
```

#### 3. Process Simulation
Mock process table with timers:

```javascript
const processes = {
    1: {pid: 1, name: 'init', cpu: 0.0, mem: 0.1},
    2: {pid: 2, name: 'kthreadd', cpu: 0.0, mem: 0.0},
    1000: {pid: 1000, name: 'bash', cpu: 0.1, mem: 0.5}
};

function psCmd(args, fs) {
    const longFormat = args.includes('-l') || args.includes('aux');
    let out = longFormat ? 
        'PID  PPID CPU MEM COMMAND\n' : 
        'PID COMMAND\n';
    
    for (const p of Object.values(processes)) {
        out += longFormat ?
            `${p.pid} 1 ${p.cpu} ${p.mem} ${p.name}\n` :
            `${p.pid} ${p.name}\n`;
    }
    return out;
}

function topCmd(args, fs) {
    let out = 'top - 12:00:00 up 1 day\n';
    out += 'Tasks: 10 total, 1 running, 9 sleeping\n\n';
    out += 'PID USER CPU MEM COMMAND\n';
    for (const p of Object.values(processes)) {
        out += `${p.pid} user ${p.cpu} ${p.mem} ${p.name}\n`;
    }
    return out;
}
```

---

## Architecture Overview

### File System Layer
```
VirtualFS
├── _resolvePath(pathStr)      // Handle ~, ., .., absolute/relative
├── _getNode(path)              // Navigate to node
├── exists(path)               // Check existence
├── isDir(path)                // Type check
├── listDir(path)              // List contents
├── readFile(path)             // Get file content
├── writeFile(path, content)   // Create/update file
├── mkdir(path)                // Create directory
├── rm(path, recursive)        // Delete
└── touch(path)                // Create empty file
```

### Command Execution Flow
```
User Input
    ↓
parseArgs() → split into tokens
    ↓
executeCommand()
    ├─ Parse redirections (>, >>)
    ├─ Route to switch statement
    ├─ Call command function(args, fs, env)
    └─ Handle output redirection
    ↓
Terminal Output
```

### Adding a New Command - 3 Steps

**Step 1**: Add case in switch statement
```javascript
case 'mycommand': output = mycommandCmd(args.slice(1), fs); break;
```

**Step 2**: Implement command function
```javascript
function mycommandCmd(args, fs) {
    if (!args.length) return '\x1b[31mmycommand: no args\x1b[0m';
    // ... implementation
    return output;
}
```

**Step 3**: Test in terminal
```bash
mycommand arg1 arg2
```

---

## Command Function Template

```javascript
function templateCmd(args, fs, env) {
    // Parse arguments
    if (!args.length) {
        return '\x1b[31mtemplate: missing operand\x1b[0m';
    }
    
    // Get flags
    const verbose = args.includes('-v');
    const recursive = args.includes('-r');
    
    // Get positional args
    const files = args.filter(a => !a.startsWith('-'));
    
    // Perform operation
    try {
        // ... your code
        return output;
    } catch (e) {
        return `\x1b[31mtemplate: ${e.message}\x1b[0m`;
    }
}
```

---

## Color Codes Reference

- **Error (Red)**: `\x1b[31m...text...\x1b[0m`
- **Success (Green)**: `\x1b[32m...text...\x1b[0m`
- **Directory (Blue)**: `\x1b[34m...text...\x1b[0m`
- **Gray (Hidden)**: `\x1b[90m...text...\x1b[0m`
- **Reset**: `\x1b[0m`

---

## Testing Checklist

For each new command, verify:
- [ ] No file specified → error message
- [ ] Invalid file → error message
- [ ] Valid input → correct output
- [ ] Flags parsed correctly
- [ ] Multiple arguments handled
- [ ] Output formatting correct
- [ ] Color codes applied

---

## Known Limitations & Future Work

| Feature | Status | Notes |
|---------|--------|-------|
| Piping (\|) | ❌ Not implemented | Would need command streaming |
| Wildcards (*) | ❌ Not implemented | Need glob pattern matching |
| Command substitution ($()) | ❌ Not implemented | Complex parsing required |
| Background jobs (&) | ❌ Not implemented | Would need async task management |
| Tab completion | ✅ Partial | Only works on filenames |
| History search (Ctrl+R) | ❌ Not implemented | Would enhance UX |
| Multi-line editing | ❌ Not implemented | Terminal limitation |

---

## Performance Tips

1. **Cache calculations**: Don't recalculate directory sizes on every `du` call
2. **Limit history**: Already capped at 100 entries
3. **Use string methods**: More efficient than regex for simple operations
4. **Avoid deep recursion**: For large virtual FS, iterate instead

---

## Testing Commands

Try these to verify implementation:

```bash
# File operations
touch test.txt
echo "hello world" > test.txt
cat test.txt
cp test.txt test_copy.txt
mv test_copy.txt test2.txt
head test.txt
tail test.txt
find . test
ls -la
rm test2.txt
rmdir newdir

# System info
df
du -s .
free
cal
date
whoami
hostname

# Search
grep hello test.txt
```
