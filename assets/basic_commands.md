## Set of commands for a browser‑based Linux terminal emulator  

| # | Command | Why it makes sense in a browser‑only environment |
|---|----------|--------------------------------------------------|
| 1 | `ls` | List files – core navigation |
| 2 | `cd` | Change directory – core navigation |
| 3 | `pwd` | Show current directory |
| 4 | `mkdir` | Create directories |
| 5 | `rmdir` | Remove empty directories |
| 6 | `touch` | Create empty files / update timestamps |
| 7 | `cp` | Copy files |
| 8 | `mv` | Move or rename files |
| 9 | `rm` | Delete files |
|10| `cat` | Display file contents |
|11| `head` | Show first lines of a file |
|12| `tail` | Show last lines of a file |
|13| `less` | Paginated view of file contents |
|14| `more` | Simple pager (fallback for `less`) |
|15| `grep` | Search text within files |
|16| `find` | Locate files by name/pattern |
|17| `chmod` | Change permission bits (simulated) |
|18| `chown` | Change ownership (simulated) |
|19| `ln` | Create symbolic/hard links |
|20| `tar` | Archive & extract files |
|21| `gzip` / `gunzip` | Compress / decompress |
|22| `bzip2` / `bunzip2` | Alternate compression |
|23| `zip` / `unzip` | ZIP archives |
|24| `df` | Show (simulated) filesystem usage |
|25| `du` | Show (simulated) directory size |
|26| `free` | Display (simulated) memory stats |
|27| `top` | Simple process list (fake) |
|28| `ps` | Show current processes (emulated) |
|29| `kill` | Terminate a fake process |
|30| `sleep` | Pause execution |
|31| `date` | Show current date/time |
|32| `cal` | Show a calendar |
|33| `uptime` | Show how long the session has run |
|34| `whoami` | Print the current user name |
|35| `who` | List logged‑in users (session‑level) |
|36| `w` | Show users and what they’re doing (session view) |
|37| `last` | Show recent login history (session‑level) |
|38| `passwd` | Change password (if you simulate auth) |
|39| `sudo` | Allow privileged‑like commands in sandbox (optional) |
|40| `ssh` | Simulated remote login (often a mock) |
|41| `scp` | Simulated secure copy |
|42| `wget` | Download files from the web |
|43| `curl` | Transfer data via URLs |
|44| `ping` | Test network reachability (may be mocked) |
|45| `traceroute` | Trace network path (mock) |
|46| `netstat` | Show network connections (simulated) |
|47| `ifconfig` / `ip` | Display interface info (mock) |
|48| `dig` / `host` / `nslookup` | DNS lookups (can be real) |
|49| `hostname` | Show/set host name (session scope) |
|50| `mount` / `umount` | Attach/detach virtual filesystems (if supported) |
|51| `echo` | Print text / expand variables |
|52| `read` | Read user input |
|53| `export` | Set environment variables |
|54| `env` | Show environment |
|55| `alias` / `unalias` | Create / remove shortcuts |
|56| `source` | Execute a script in the current session |
|57| `diff` | Compare two files |
|58| `patch` | Apply a diff to a file |
|59| `man` | Show manual pages (usually static files) |
|60| `cat /proc/cpuinfo` | Display static CPU info (if you provide a mock file) |
|61| `cat /proc/meminfo` | Display static memory info (mock) |
|62| `dmesg` | Show kernel messages (mock) |
|63| `tail -f <log>` | Follow a log file (if you expose log files) |
|64| `crontab` | Edit per‑session scheduled tasks (optional) |
|65| `at` | Schedule a one‑off command (optional) |