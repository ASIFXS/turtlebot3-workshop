# ERR 1 — Errors During Cleanup & Prerequisites

> ← Back to [STEP_1_clean_and_prereqs.md](../steps/STEP_1_clean_and_prereqs.md)

---

## ❌ `dpkg -l | grep gazebo` still shows packages after removal

**Cause:** Some packages have unusual names not caught by the wildcard.

**Fix:**
```bash
# List exactly what's installed
dpkg -l | grep -i gazebo
dpkg -l | grep -i ignition

# Remove each one manually
sudo apt remove --purge <package-name> -y
sudo apt autoremove -y
```

---

## ❌ `sudo apt remove` fails with "Unable to lock the administration directory"

**Cause:** Another apt process is running (update manager, unattended upgrades).

**Fix:**
```bash
# Wait and try again, or kill the lock
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock
sudo dpkg --configure -a
sudo apt remove --purge '*gazebo*' -y
```

---

## ❌ `vcs --version` not found after installing python3-vcstool

**Cause:** pip-installed vcstool not in PATH, or apt install failed silently.

**Fix:**
```bash
# Try apt again
sudo apt install python3-vcstool -y

# Or install via pip
pip3 install vcstool

# Check where it installed
which vcs
# If not found:
export PATH=$PATH:~/.local/bin
echo "export PATH=$PATH:~/.local/bin" >> ~/.bashrc
```

---

## ❌ `sudo apt update` fails with "Failed to fetch" errors

**Cause:** Network issue or outdated repository keys.

**Fix:**
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY_FROM_ERROR>
sudo apt update
```

---

## ❌ System upgrade breaks something / partial upgrade

**Fix:**
```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
sudo apt upgrade -y
```
