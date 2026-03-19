# ERR 3 — Errors During Workspace Setup & vcstool

> ← Back to [STEP_3_workspace_vcstool.md](../steps/STEP_3_workspace_vcstool.md)

---

## ❌ `vcs import src < turtlebot3_humble.repos` fails / partial clone

**Cause:** Network timeout or wrong file location.

**Fix:**
```bash
# Make sure you are in the right directory
cd ~/turtlebot3_ws
ls  # Should show: src/  turtlebot3_humble.repos

# Try again
vcs import src < turtlebot3_humble.repos

# If one repo failed, you can re-run — vcs skips already-cloned repos
```

---

## ❌ `vcs: command not found`

**Fix:**
```bash
sudo apt install python3-vcstool -y
# Or:
pip3 install vcstool
export PATH=$PATH:~/.local/bin
```

---

## ❌ Wrong branch / version mismatch error

```
error: pathspec 'humble' did not match any file(s) known to git
```

**Cause:** The repo doesn't have a `humble` branch.

**Fix:** Check the correct branch name on GitHub:
```bash
# For each repo, check available branches
git ls-remote --heads https://github.com/ROBOTIS-GIT/turtlebot3.git | grep humble
```

The `.repos` file provided in this guide uses verified `humble` branch names.

---

## ❌ `rosdep init` fails — "file already exists"

This is **not an error**. It means rosdep was already initialized.

```bash
# Just skip init and run update only
rosdep update
```

---

## ❌ `rosdep update` fails — network error

```bash
# Try with a timeout increase
rosdep update --include-eol-distros
# Or just retry — usually a temporary network issue
```

---

## ❌ src/ directory is empty after vcs import

**Cause:** You ran `vcs import` from the wrong directory.

**Fix:**
```bash
cd ~/turtlebot3_ws           # Must be here
ls                           # Should show src/ and turtlebot3_humble.repos
vcs import src < turtlebot3_humble.repos
ls src/                      # Should now show turtlebot3/ and utils/
```
