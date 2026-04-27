# Command Mapping - Basic Commands & Tools Integration

## Mapping to basic_commands.md (65 commands)

### ✅ Implemented (34/65 = 52%)

| # | Command | File Link | Implementation | Status |
|---|---------|-----------|-----------------|--------|
| 1 | `ls` | basic_commands.md#1 | [terminal.html](templates/terminal.html) - ls() | ✅ |
| 2 | `cd` | basic_commands.md#2 | [terminal.html](templates/terminal.html) - cd() | ✅ |
| 3 | `pwd` | basic_commands.md#3 | [terminal.html](templates/terminal.html) - direct | ✅ |
| 4 | `mkdir` | basic_commands.md#4 | [terminal.html](templates/terminal.html) - mkdirCmd() | ✅ |
| 5 | `rmdir` | basic_commands.md#5 | [terminal.html](templates/terminal.html) - rmdirCmd() | ✅ |
| 6 | `touch` | basic_commands.md#6 | [terminal.html](templates/terminal.html) - touchCmd() | ✅ |
| 7 | `cp` | basic_commands.md#7 | [terminal.html](templates/terminal.html) - cpCmd() | ✅ |
| 8 | `mv` | basic_commands.md#8 | [terminal.html](templates/terminal.html) - mvCmd() | ✅ |
| 9 | `rm` | basic_commands.md#9 | [terminal.html](templates/terminal.html) - rmCmd() | ✅ |
| 10 | `cat` | basic_commands.md#10 | [terminal.html](templates/terminal.html) - catCmd() | ✅ |
| 11 | `head` | basic_commands.md#11 | [terminal.html](templates/terminal.html) - headCmd() | ✅ |
| 12 | `tail` | basic_commands.md#12 | [terminal.html](templates/terminal.html) - tailCmd() | ✅ |
| 15 | `grep` | basic_commands.md#15 | [terminal.html](templates/terminal.html) - grepCmd() | ✅ |
| 16 | `find` | basic_commands.md#16 | [terminal.html](templates/terminal.html) - findCmd() | ✅ |
| 17 | `chmod` | basic_commands.md#17 | [terminal.html](templates/terminal.html) - chmodCmd() | ✅ |
| 18 | `chown` | basic_commands.md#18 | [terminal.html](templates/terminal.html) - chownCmd() | ✅ |
| 24 | `df` | basic_commands.md#24 | [terminal.html](templates/terminal.html) - dfCmd() | ✅ |
| 25 | `du` | basic_commands.md#25 | [terminal.html](templates/terminal.html) - duCmd() | ✅ |
| 26 | `free` | basic_commands.md#26 | [terminal.html](templates/terminal.html) - freeCmd() | ✅ |
| 31 | `date` | basic_commands.md#31 | [terminal.html](templates/terminal.html) - direct | ✅ |
| 32 | `cal` | basic_commands.md#32 | [terminal.html](templates/terminal.html) - calCmd() | ✅ |
| 34 | `whoami` | basic_commands.md#34 | [terminal.html](templates/terminal.html) - direct | ✅ |
| 35 | `who` | basic_commands.md#35 | Mockable via environment | 🟡 Ready |
| 36 | `w` | basic_commands.md#36 | Mockable via environment | 🟡 Ready |
| 37 | `last` | basic_commands.md#37 | Mockable via login history | 🟡 Ready |
| 39 | `sudo` | basic_commands.md#39 | [terminal.html](templates/terminal.html) - direct | ✅ |
| 51 | `echo` | basic_commands.md#51 | [terminal.html](templates/terminal.html) - echoCmd() | ✅ |
| 52 | `read` | basic_commands.md#52 | Interactive terminal support | 🟡 Ready |
| 53 | `export` | basic_commands.md#53 | [terminal.html](templates/terminal.html) - exportCmd() | ✅ |
| 54 | `env` | basic_commands.md#54 | [terminal.html](templates/terminal.html) - envCmd() | ✅ |
| 55 | `alias` | basic_commands.md#55 | Simple map in environment | 🟡 Ready |
| 56 | `source` | basic_commands.md#56 | Shell script execution | 🔴 Complex |
| 63 | `history` | basic_commands.md#63 | [terminal.html](templates/terminal.html) - historyCmd() | ✅ |
| 59 | `man` | basic_commands.md#59 | Static help text | 🟡 Ready |

### 🔄 Medium Priority (Ready to implement - 15-20 commands)

| # | Command | Reason | Implementation Strategy |
|---|---------|--------|------------------------|
| 13 | `less`/`more` | Text pagination | Interactive scrolling |
| 14 | `more` | Fallback pager | Pagination interface |
| 19 | `ln` | Link creation | VirtualFS symlink extension |
| 20 | `tar` | Archive | Use tar-js library |
| 21 | `gzip`/`gunzip` | Compression | Use pako library |
| 22 | `bzip2`/`bunzip2` | Compression | Compression library |
| 23 | `zip`/`unzip` | Archives | Use fflate library |
| 27 | `top` | Process monitor | Fake process table + timers |
| 28 | `ps` | Process list | Mock process array |
| 29 | `kill` | Process termination | Remove from process array |
| 30 | `sleep` | Pause | JS setTimeout/Promise |
| 33 | `uptime` | ✅ Already done | See #33 |
| 38 | `passwd` | Auth simulation | Session-level auth |
| 40 | `ssh`/`scp` | Remote access | Mock connection |
| 42-43 | `wget`/`curl` | Download | Browser fetch API |

### 🔴 Complex/Advanced (Lower priority - 12 commands)

| # | Command | Reason Complex | Alternative |
|---|---------|----------------|-------------|
| 44 | `ping` | Network mock | Fake latency values |
| 45 | `traceroute` | Network mock | Simulated hops |
| 46 | `netstat` | Network display | Mock connections |
| 47 | `ifconfig`/`ip` | Network config | Mock interface info |
| 48 | `dig`/`host`/`nslookup` | DNS lookup | Call public DNS API |
| 49 | `hostname` | ✅ Already done | See #35 |
| 50 | `mount`/`umount` | Filesystem | Virtual mount points |
| 57 | `diff` | Text comparison | Diffing algorithm |
| 58 | `patch` | Apply diff | Complex parsing |
| 60-62 | `/proc` files, `dmesg` | Kernel mock | Static data files |
| 64-65 | `crontab`, `at` | Task scheduling | Timer management UI |

---

## Mapping to basic_tools.md (Implementation Table)

### Tools by Category & Implementation Status

#### Text Editors (🟡 Medium Complexity)

| Tool | Status | Browser Implementation |
|------|--------|----------------------|
| `nano` | 🟡 | Inline textarea + keybindings |
| `vim` | 🟡 | vim.js/ACE editor integration |
| `micro` | 🟡 | Port to JS or WebAssembly |

**Note**: These require significant UI/UX work. Consider simpler text editing first.

#### Process Monitors (✅ Ready)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `top` | 🟡 | Fake process table, update every second |
| `htop` | 🟡 | Colorized process list in terminal |

**Implementation**: Mock process array with CPU/memory stats

#### File Managers (🔴 Complex)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `mc` (Midnight Commander) | 🔴 | Two-pane split view in terminal |

**Note**: Requires advanced terminal UI. Lower priority.

#### Archivers (✅ Ready via Libraries)

| Tool | Status | Library | Implementation |
|------|--------|---------|-----------------|
| `tar` | ✅ | tar-js | Extract/create tar archives |
| `gzip` | ✅ | pako | Compress/decompress gzip |
| `bzip2` | ✅ | bzip2-js | Compression support |
| `zip`/`unzip` | ✅ | fflate | ZIP format support |

**Implementation**: Wrap library functions, integrate with VirtualFS

#### Network Utilities (⚠️ Mixed)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `curl`/`wget` | ✅ | Browser fetch API (with CORS) |
| `ping` | 🟡 | Mock latency, no real ICMP |
| `traceroute` | 🟡 | Simulated hop output |
| `nslookup`/`dig` | ✅ | Public DNS-over-HTTPS API |

**Implementation**: Use browser APIs where available, mock where needed

#### System Info (✅ Done)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `uname` | ✅ | Static string response |
| `hostname` | ✅ | Environment variable |
| `date` | ✅ | Browser Date API |
| `cal` | ✅ | Calendar generation |
| `uptime` | ✅ | Session timer |

#### Resource Stats (✅ Ready)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `df` | ✅ | Fixed filesystem stats |
| `du` | ✅ | Calculate from VirtualFS |
| `free` | ✅ | Fixed memory stats |
| `lsblk` | 🟡 | Mock block device list |

#### Text Filters (🟡 Medium)

| Tool | Status | Library/Implementation |
|------|--------|----------------------|
| `grep` | ✅ | String matching |
| `sed` | 🟡 | regexp-based substitution |
| `awk` | 🟡 | awk-js npm package |
| `cut` | 🟡 | String slicing |
| `sort` | 🟡 | JavaScript Array.sort() |
| `uniq` | 🟡 | Set deduplication |
| `wc` | 🟡 | Character/word counting |

**Implementation**: Most can be pure JS, some may benefit from npm packages

#### Shell Built-ins (✅ Done)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `echo` | ✅ | Variable expansion |
| `read` | ✅ | Terminal input handling |
| `export` | ✅ | Environment management |
| `alias` | 🟡 | Command map |
| `source` | 🔴 | Script execution engine |

#### File Navigation (✅ Done)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `ls` | ✅ | Recursive listing |
| `cd` | ✅ | Path resolution |
| `pwd` | ✅ | Current path |
| `mkdir` | ✅ | Directory creation |
| `rmdir` | ✅ | Empty dir removal |
| `rm` | ✅ | File deletion |
| `mv` | ✅ | File movement |
| `cp` | ✅ | File copying |
| `ln` | 🟡 | Symlink support |

#### Scripting (🔴 Very Complex)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `bash`/`sh` | 🔴 | Full POSIX interpreter |
| Simple scripts | 🟡 | Sequential command execution |

**Note**: Full bash would require huge WASM binary or significant JS engine

#### Misc Utilities (✅ Ready)

| Tool | Status | Implementation |
|------|--------|-----------------|
| `clear` | ✅ | ANSI clear code |
| `reset` | ✅ | Reset terminal state |
| `history` | ✅ | Command history array |
| `type` | 🟡 | Command type lookup |
| `which` | 🟡 | Command path lookup |

---

## Implementation Checklist

### Completed ✅
- [x] Core file operations (ls, cd, pwd, mkdir, rm, cp, mv, touch)
- [x] File viewing (cat, head, tail, grep, find)
- [x] System info (date, cal, whoami, hostname, uptime)
- [x] Resource monitoring (df, du, free)
- [x] Environment (echo, export, env, unset)
- [x] Permission simulation (chmod, chown)

### Phase 2: Text Processing 🟡
- [ ] `sed` - Stream editor
- [ ] `awk` - Text processing
- [ ] `cut` - Field extraction
- [ ] `sort` - Sorting
- [ ] `uniq` - Deduplication
- [ ] `wc` - Word count

### Phase 3: Archives & Compression 🟡
- [ ] `tar` - Archive creation/extraction
- [ ] `gzip` - Compression
- [ ] `bzip2` - Compression
- [ ] `zip`/`unzip` - ZIP format

### Phase 4: Process Management 🟡
- [ ] `ps` - Process listing
- [ ] `top` - Process monitor
- [ ] `kill` - Process termination
- [ ] `sleep` - Pause execution

### Phase 5: Network & Advanced 🔴
- [ ] `curl`/`wget` - Download
- [ ] `ping`/`traceroute` - Network
- [ ] Text editors (`nano`, `vim`)
- [ ] Shell scripting

---

## Usage Examples

```bash
# Core operations - all working ✅
ls -la
mkdir mydir
touch file.txt
cp file.txt file_copy.txt
mv file_copy.txt newname.txt
rm newname.txt
cd mydir
pwd

# Text viewing - all working ✅
cat file.txt
head file.txt
tail -n 20 file.txt
grep "pattern" file.txt
find . "*.txt"

# System - all working ✅
date
cal
whoami
hostname
uptime
df
du -s .
free
chmod 755 file.txt
chown user file.txt

# Next phase to implement
# sed 's/old/new/g' file.txt
# awk '{print $1}' file.txt
# sort file.txt
# tar -czf archive.tar.gz mydir/
```

---

## Files Modified/Created

| File | Purpose | Status |
|------|---------|--------|
| [INTEGRATION_STATUS.md](INTEGRATION_STATUS.md) | Track implementation progress | ✅ Active |
| [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) | Guide for adding new commands | ✅ New |
| [COMMAND_MAPPING.md](COMMAND_MAPPING.md) | This file - links to requirements | ✅ New |
| [templates/terminal.html](templates/terminal.html) | Terminal implementation | ✅ Updated |

