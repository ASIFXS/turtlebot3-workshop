# STEP 1 — Clean System & Install Prerequisites

> ⚠️ **Got an error in this step?** → See [ERR_1_clean_prereqs.md](../errors/ERR_1_clean_prereqs.md)

---

## 1.1 — Remove All Old Gazebo Installations

If you have any previous Gazebo or Ignition install, remove it completely first.
Leftover files cause plugin conflicts and black screens later.

```bash
sudo apt remove --purge '*gazebo*' -y
sudo apt remove --purge '*ignition*' -y
sudo apt remove --purge 'ros-*gazebo*' -y
sudo apt autoremove -y
sudo apt autoclean
```

Verify nothing remains:
```bash
dpkg -l | grep -i gazebo
# Should return NOTHING. If you see entries, run the remove commands again.
```

---

## 1.2 — Update System

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 1.3 — Install Prerequisites

```bash
sudo apt install -y \
  curl \
  gnupg2 \
  lsb-release \
  software-properties-common \
  python3-pip \
  python3-vcstool \
  python3-colcon-common-extensions \
  python3-rosdep \
  git \
  build-essential
```

Verify key tools:
```bash
vcs --version        # Should show: vcstool X.X.X
git --version        # Should show: git version X.X.X
python3 --version    # Should show: Python 3.10.X
```

---

## ✅ Checklist Before Moving On

- [ ] `dpkg -l | grep gazebo` returns nothing
- [ ] `vcs --version` works
- [ ] `git --version` works
- [ ] System is updated

➡️ **Next:** [STEP_2_ros2_humble.md](STEP_2_ros2_humble.md)
