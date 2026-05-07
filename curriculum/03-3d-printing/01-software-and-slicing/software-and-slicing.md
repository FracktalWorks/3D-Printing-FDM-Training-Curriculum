# Module 3: Software Tools for 3D Printing

> Git, GitHub, VS Code, SSH, Linux command line, and Cirkit Designer — the software stack every 3D printing technician uses daily to manage firmware, configurations, and printer infrastructure.

![FDM printer executing a print from slicer-generated G-code — the output of software tools like Fracktory, VS Code, and Git-managed configs](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/3D_printer2.jpg/400px-3D_printer2.jpg)
*An FDM printer executing a print from slicer-generated G-code. The software tools in this module (Git, VS Code, SSH, Fracktory/Cura) are all used to prepare, configure, and monitor prints like this. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:3D_printer2.jpg), CC BY-SA 3.0*

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Use Git and GitHub to track configuration files and firmware changes
- Navigate the Linux command line for Raspberry Pi and printer host management
- Connect to a remote machine via SSH and transfer files
- Use VS Code as an editor for Klipper configs, G-code, and scripts
- Use Cirkit Designer to document electrical schematics
- Manage software environments using package managers

## Prerequisites

- Basic computer literacy (file browser, web browser, copy/paste)
- Module 1: Electronics Basics (context for what you'll be configuring)

---

## 🛠️ Tools Required

| Tool | Purpose |
|------|---------|
| Laptop / desktop with internet access | Git, VS Code, SSH client |
| [Git](https://git-scm.com/downloads) (v2.40+) | Version control — required for all config management |
| [VS Code](https://code.visualstudio.com/) | Code editor with Remote SSH, GitLens extensions |
| SSH client (built-in on macOS/Linux; OpenSSH on Windows) | Connecting to printer Raspberry Pi hosts |
| [GitHub account](https://github.com) | Hosting printer config repositories |
| [Cirkit Designer account](https://app.cirkitdesigner.com/) | Browser-based schematic tool — no install required |
| Network access to printer LAN (192.168.1.101–104) | SSH and OctoPrint web interface access |

> 💡 **Optional but recommended:** Windows Terminal (better SSH experience on Windows) and WSL2 (native Linux commands on Windows).

---

## ⚠️ Safety Guidelines

1. **Never commit secrets to GitHub.** API keys, passwords, and Wi-Fi credentials in a public repo are exposed immediately to automated scanners. Use environment variables or `.gitignore` exclusions.
2. **Never force-push to `main`.** `git push --force` on the main branch destroys shared history. Always use a feature branch + pull request workflow.
3. **Verify the machine alias before `sudo` commands.** Always run `hostname` after SSH to confirm which machine you are connected to before any destructive command.
4. **SSH keys over passwords.** Password authentication is susceptible to brute-force. Use SSH key pairs for all printer host access.
5. **Don't run untrusted scripts as root.** Read any script before executing with `sudo`. Verify the source URL before using `curl | sudo bash` patterns.
6. **Backup before editing `printer.cfg`.** Commit the current working config to Git before making changes. A corrupted config that can't be reverted causes unplanned downtime.

---

## 1. Git and GitHub

**Git** is a **version control system** — it tracks every change you make to a file so you can go back to any previous version. Think of it as an infinite undo history with timestamps and author notes.

**GitHub** is a cloud hosting platform for Git repositories. Our printer configurations, firmware settings, and training materials are stored here.

### 1.1 Why Version Control Matters for 3D Printing

Every time you change a Klipper `printer.cfg`, Marlin `Configuration.h`, or slicer profile, you risk breaking something that was working. With Git:
- Every change is recorded with a message: `"Increased Z-offset to +0.05 after bed swap"`
- You can instantly revert a bad change: `git revert`
- Multiple people can collaborate on the same config file

### 1.2 Core Git Concepts

| Term | Meaning |
|------|---------|
| **Repository (repo)** | A folder tracked by Git containing all files and their history |
| **Commit** | A saved snapshot of changes with a message |
| **Branch** | A parallel version of the repo for testing changes |
| **Clone** | Download a copy of a remote repo to your machine |
| **Pull** | Fetch and merge the latest changes from remote |
| **Push** | Upload your local commits to the remote (GitHub) |
| **Diff** | Shows what changed between two versions |
| **Merge** | Combines changes from two branches |

### 1.3 Git Setup (First Time)

```bash
# Set your identity — appears in commit history
git config --global user.name "Your Name"
git config --global user.email "you@company.com"

# Verify
git config --list
```

### 1.4 Daily Git Workflow

```bash
# 1. Clone a repository from GitHub to your machine
git clone https://github.com/your-org/printer-configs.git
cd printer-configs

# 2. Check current status (what's changed?)
git status

# 3. See exactly what changed in a file
git diff printer.cfg

# 4. Stage changes for commit
git add printer.cfg
# Or stage everything
git add .

# 5. Commit with a meaningful message
git commit -m "Tune PID values for Dragon hotend after nozzle swap"

# 6. Push to GitHub
git push origin main

# 7. Pull latest changes from team
git pull origin main
```

### 1.5 Managing Printer Configs with Git

**Recommended repo structure for a printer farm:**

```
printer-farm-configs/
├── snowflake/
│   ├── printer.cfg
│   ├── macros.cfg
│   └── slicer-profiles/
├── printer-configs/
│   ├── printer.cfg
│   └── macros.cfg
├── dragon/
│   ├── printer.cfg
│   └── macros.cfg
└── twin-dragon/
    ├── printer.cfg
    └── macros.cfg
```

**Best practice:** Commit config changes BEFORE printing. If the print fails due to a bad config, you can check `git log` to see what changed.

### 1.6 Branching for Experiments

```bash
# Create a new branch to test faster print speeds
git checkout -b experiment/faster-speeds

# Make changes, commit them
git add printer.cfg
git commit -m "Test 200mm/s on Dragon — experimental"

# If experiment works, merge back to main
git checkout main
git merge experiment/faster-speeds

# If experiment fails, just delete the branch
git checkout main
git branch -d experiment/faster-speeds
```

---

## 2. VS Code

**Visual Studio Code (VS Code)** is a free, open-source code editor built by Microsoft. It is the recommended editor for:
- Klipper `printer.cfg` and macro files
- Marlin `Configuration.h` / `Configuration_adv.h`
- G-code review
- Python scripts for automation
- SSH remote editing (edit files directly on the Raspberry Pi)

### 2.1 Installation

1. Download from: https://code.visualstudio.com/
2. Install with defaults.
3. Launch VS Code.

### 2.2 Essential Extensions for 3D Printing Work

Install these from the VS Code Extensions panel (`Ctrl+Shift+X`):

| Extension | Purpose |
|-----------|---------|
| **Remote - SSH** | Edit files on Raspberry Pi directly from VS Code |
| **Python** | Syntax highlighting, linting for Python scripts |
| **GitLens** | Inline Git blame, history, and change visualization |
| **Markdown All in One** | Preview, editing, and table formatting for .md files |
| **GCode** | Syntax highlighting for G-code files |

### 2.3 Key Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + P` | Quick open any file by name |
| `Ctrl + Shift + P` | Command palette (run any VS Code command) |
| `Ctrl + ~` | Open integrated terminal |
| `Ctrl + /` | Toggle line comment |
| `Ctrl + F` | Find in current file |
| `Ctrl + H` | Find and replace |
| `Ctrl + Z` | Undo |
| `Alt + Z` | Toggle word wrap |
| `F12` | Go to definition |

### 2.4 Editing Klipper Config in VS Code

1. Open the terminal (`Ctrl + ~`).
2. SSH to the Raspberry Pi (see Section 4).
3. In VS Code Remote Explorer, connect to the Pi.
4. Navigate to `~/printer_data/config/printer.cfg`.
5. Edit the file — changes are saved directly on the Pi.
6. In OctoPrint, go to the **Terminal** tab and send `FIRMWARE_RESTART` to apply changes.

---

## 3. Linux Command Line Basics

The Raspberry Pi CM4 running Klipper uses **Linux (OctoPi OS)**. You must be comfortable with the terminal.

### 3.1 Essential Commands

```bash
# Navigation
pwd                    # Print current directory
ls                     # List files in current directory
ls -la                 # List with details + hidden files
cd /path/to/folder     # Change directory
cd ..                  # Go up one level
cd ~                   # Go to home directory

# File operations
cp source.txt dest.txt       # Copy file
mv file.txt new_name.txt     # Move or rename file
rm file.txt                  # Delete file (PERMANENT — no recycle bin)
rm -rf folder/               # Delete folder and all contents (use with caution)
mkdir new_folder             # Create directory
cat file.txt                 # Print file contents
less file.txt                # View file with scrolling (q to quit)
nano file.txt                # Simple text editor in terminal
grep "pattern" file.txt      # Search for text in file

# System info
df -h                        # Disk usage (human readable)
free -h                      # RAM usage
top                          # Live process monitor (q to quit)
uname -a                     # OS and kernel version
hostname -I                  # Get IP address

# Process management
ps aux                       # List all running processes
kill PID                     # Kill process by ID
sudo systemctl status klipper   # Check Klipper service status
sudo systemctl restart klipper  # Restart Klipper

# Package management (Raspberry Pi OS / Debian)
sudo apt update              # Refresh package list
sudo apt upgrade             # Install updates
sudo apt install package-name  # Install new software
```

### 3.2 File Permissions

Linux uses a permissions system: **owner / group / others** × **read / write / execute**.

```bash
ls -la
# Output example:
# -rwxr-xr-x 1 pi pi 4096 Jan 1 10:00 script.py
#  ↑↑↑ owner: rwx (read, write, execute)
#     ↑↑↑ group: r-x (read, execute only)
#        ↑↑↑ others: r-x

chmod +x script.py          # Make script executable
chmod 755 script.py         # rwxr-xr-x in numeric notation
sudo chown pi:pi file.txt   # Change owner to user 'pi', group 'pi'
```

### 3.3 Redirects and Pipes

```bash
# Redirect output to a file (overwrite)
klipper_log > /tmp/klipper_snapshot.txt

# Append to file
echo "Test complete" >> log.txt

# Pipe: send output of one command to input of another
cat klipper.log | grep "error"   # Show only lines containing "error"
dmesg | tail -20                  # Show last 20 kernel messages
```

---

## 4. SSH — Secure Shell

**SSH (Secure Shell)** lets you securely control a remote Linux machine (like the Raspberry Pi running your printer) from your laptop over a network.

### 4.1 Connecting via SSH

**On Windows (PowerShell or Windows Terminal):**

```powershell
ssh pi@192.168.1.100
# Replace 192.168.1.100 with your Raspberry Pi's IP address
# Default username: pi
# Default password: raspberry (CHANGE THIS immediately on new installs)
```

**First-time connection:** You'll see a fingerprint warning — type `yes` to accept.

**Finding the Pi's IP address:**
```bash
# On the Pi (if you have direct access):
hostname -I

# On your router: Look at DHCP leases for a device named "raspberrypi"
# Or use network scanner: nmap -sn 192.168.1.0/24
```

### 4.2 SSH Keys (Passwordless Login)

Repeatedly typing passwords is slow and insecure. Set up SSH key authentication:

```powershell
# On your laptop — generate a key pair (run once)
ssh-keygen -t ed25519 -C "your@email.com"
# Accept defaults, set a passphrase if desired

# Copy your public key to the Raspberry Pi
ssh-copy-id pi@192.168.1.100
# Enter password once

# Now login is instant — no password needed
ssh pi@192.168.1.100
```

### 4.3 Transferring Files via SCP

**SCP (Secure Copy)** copies files over SSH:

```bash
# Copy a file FROM your laptop TO the Pi
scp printer.cfg pi@192.168.1.100:~/printer_data/config/

# Copy a file FROM the Pi TO your laptop
scp pi@192.168.1.100:~/klipper.log ./klipper_backup.log

# Copy an entire folder
scp -r ./slicer-profiles/ pi@192.168.1.100:~/configs/
```

### 4.4 SSH Config File (Multiple Printers)

Instead of remembering IP addresses, create an SSH config file:

```bash
# On your laptop: ~/.ssh/config (Linux/Mac) or C:\Users\YourName\.ssh\config (Windows)

Host snowflake
    HostName 192.168.1.101
    User pi
    IdentityFile ~/.ssh/id_ed25519

Host julia
    HostName 192.168.1.102
    User pi

Host dragon
    HostName 192.168.1.103
    User pi

Host twin-dragon
    HostName 192.168.1.104
    User pi
```

Now connect with: `ssh snowflake` instead of the full address.

### 4.5 Security Best Practices for SSH

1. **Change default password** immediately: `passwd`
2. **Disable password authentication** after setting up SSH keys — edit `/etc/ssh/sshd_config`, set `PasswordAuthentication no`
3. **Change default port** (optional): `Port 2222` in sshd_config
4. **Keep the Pi updated**: `sudo apt update && sudo apt upgrade`
5. **Never expose SSH port directly to the internet** without a VPN or reverse proxy

---

## 5. GitHub Workflow for Printer Configs

### 5.1 Setting Up a Config Repository

```bash
# On your laptop
mkdir printer-configs
cd printer-configs
git init
git remote add origin https://github.com/your-org/printer-configs.git

# Create initial structure
mkdir -p snowflake julia dragon twin-dragon
touch snowflake/printer.cfg julia/printer.cfg dragon/printer.cfg twin-dragon/printer.cfg

git add .
git commit -m "Initial config structure for all 4 printers"
git push -u origin main
```

### 5.2 Pulling Config Updates to a Printer's Pi

```bash
# SSH into the printer's Pi
ssh snowflake

# Clone the config repo (first time only)
git clone https://github.com/your-org/printer-configs.git ~/printer_configs

# Symlink the config to where Klipper expects it
ln -s ~/printer_configs/snowflake/printer.cfg ~/printer_data/config/printer.cfg

# When configs are updated on GitHub, pull on the Pi
cd ~/printer_configs && git pull origin main
```

---

## 6. Cirkit Designer for Wiring Documentation

**Cirkit Designer** (https://app.cirkitdesigner.com/) is used to create wiring schematics that are committed to GitHub alongside printer configs.

### 6.1 Why Document Wiring in Software

When a printer is serviced 6 months later by a different technician:
- Without documentation: 2–4 hours tracing wires
- With a Cirkit Designer schematic in the repo: 10 minutes

### 6.2 Workflow

1. Open https://app.cirkitdesigner.com/ and create a project named after the printer (e.g., `Snowflake-Wiring`).
2. Add the MKS board, PSU, motors, endstops, and sensors from the component library.
3. Wire all connections as built on the actual printer.
4. Export as **PNG** and **PDF**.
5. Save PNG and PDF into the printer's config folder in Git:
   ```
   snowflake/
   ├── printer.cfg
   ├── macros.cfg
   └── wiring/
       ├── snowflake-wiring-v1.png
       └── snowflake-wiring-v1.pdf
   ```
6. Commit and push.

---

## ❌ Common Mistakes

| Mistake | What Happens | Correct Practice |
|---------|-------------|------------------|
| Committing `printer.cfg` without testing the change | Broken config pushed to team repo | Always `FIRMWARE_RESTART` and test before committing |
| Using `git add .` without reviewing changes | Accidentally commits temp files, logs, or secrets | Use `git status` first, then `git add <specific-file>` |
| Editing `printer.cfg` directly via Nano on the Pi | Changes not tracked in Git | Edit via VS Code Remote SSH so changes are tracked |
| SSH password reuse across machines | One compromised machine means all are compromised | Unique SSH keys or strong unique passwords per host |
| No `.gitignore` for temp/log files | Repo bloat with binary and log files | Add `*.log`, `.tmp/`, `*.bak` to `.gitignore` |
| Not running `SAVE_CONFIG` after calibration | Calibration values lost on next Klipper restart | Always run `SAVE_CONFIG` immediately after calibration |
| Wrong line endings (CRLF on Windows) in `.cfg` files | Klipper parse errors on Linux | Set VS Code end-of-line to LF (`\n`) for all Klipper config files |
| SSH connection dropped mid-edit (long session) | Unsaved changes lost | Use `tmux` or `screen` sessions for long Pi operations |

---

## 7. Hands-On Exercises

### Exercise 3.1 — Git Basics
- [ ] Install Git on your laptop (`git --version` should print a version number)
- [ ] Clone the team printer-configs repository
- [ ] Make a change to a `README.md` file and commit it with a descriptive message
- [ ] Push the commit to GitHub and verify it appears on the website

### Exercise 3.2 — VS Code Setup
- [ ] Install VS Code and all 5 recommended extensions
- [ ] Open the printer-configs repository in VS Code
- [ ] Use GitLens to view the commit history of `printer.cfg`
- [ ] Use the integrated terminal to run `git log --oneline`

### Exercise 3.3 — SSH to a Raspberry Pi
- [ ] Find the IP address of the Snowflake Raspberry Pi on the local network
- [ ] SSH in using username and password
- [ ] Run `df -h` to check available disk space
- [ ] Set up SSH key authentication so you no longer need a password
- [ ] Add the printer to your SSH config file with an alias

### Exercise 3.4 — Linux Command Line
- [ ] Navigate to the Klipper config directory (`~/printer_data/config/`)
- [ ] View `printer.cfg` using `cat` and then `less`
- [ ] Use `grep` to find all lines containing `[stepper_x]` in printer.cfg
- [ ] Check if Klipper service is running: `sudo systemctl status klipper`

### Exercise 3.5 — Cirkit Designer
- [ ] Create a new Cirkit Designer project
- [ ] Place an MKS board and a NEMA 17 motor
- [ ] Wire the motor to the X-motor port
- [ ] Export as PNG and commit to the team's config repository

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Git and GitHub for Beginners](https://www.youtube.com/watch?v=RGOj5yH7evk) | freeCodeCamp | 1-hour complete Git crash course — covers all daily commands |
| [Linux Command Line Crash Course](https://www.youtube.com/watch?v=ZtqBQ68cfJc) | freeCodeCamp | Terminal basics from scratch — `ls` to file permissions |
| [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) | Traversy Media | SSH setup, keys, and SCP explained simply |
| [VS Code for Beginners](https://www.youtube.com/watch?v=VqCgcpAypFQ) | Programming with Mosh | Interface overview, extensions, and shortcuts |
| [SSH into Raspberry Pi from Windows](https://www.youtube.com/watch?v=a6KcVtp-6po) | NetworkChuck | Practical Raspberry Pi SSH setup from Windows |

---

## 📚 Further Reading

- [Git Official Documentation](https://git-scm.com/doc) — Complete command reference
- [GitHub Docs — Hello World Guide](https://docs.github.com/en/get-started/quickstart/hello-world) — Official GitHub beginner tutorial
- [SSH Academy](https://www.ssh.com/academy/ssh) — Comprehensive SSH reference and best practices
- [Linux Command Reference](https://linuxcommand.org/lc3_learning_the_shell.php) — Shell commands from zero
- [Cirkit Designer Documentation](https://app.cirkitdesigner.com/) — Official tool reference

---

## ✅ Knowledge Check

1. What Git command shows you what has changed in your working directory since the last commit?
2. You made a change to `printer.cfg` that broke the printer. How do you see what changed and revert it?
3. What is the difference between `git pull` and `git clone`?
4. What Linux command would you use to find all occurrences of `"pid_kp"` in a file named `printer.cfg`?
5. You want to copy a local file called `new_macros.cfg` to the Raspberry Pi at `192.168.1.105`. Write the exact SCP command.
6. What is the purpose of SSH key authentication over password authentication?
7. Name three VS Code extensions useful for 3D printer firmware/config work and explain what each does.

---

*[← Section Index](./README.md) | [🏠 Curriculum Index](../../README.md) | [Next: Filaments & Materials →](../02-filaments-and-materials/README.md)*
