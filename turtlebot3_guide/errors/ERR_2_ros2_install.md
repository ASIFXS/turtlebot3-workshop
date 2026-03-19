# ERR 2 — Errors During ROS 2 Humble Install

> ← Back to [STEP_2_ros2_humble.md](../steps/STEP_2_ros2_humble.md)

---

## ❌ `sudo apt install ros-humble-desktop` fails with "Unable to locate package"

**Cause:** ROS 2 repository was not added correctly.

**Fix:**
```bash
# Check if the repo file exists
cat /etc/apt/sources.list.d/ros2.list

# If missing or wrong, re-add it:
sudo rm /etc/apt/sources.list.d/ros2.list

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
  http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt install ros-humble-desktop -y
```

---

## ❌ Wrong Ubuntu version — `ros-humble-desktop` not available

**Cause:** Humble only supports Ubuntu 22.04 (Jammy).

**Check your version:**
```bash
lsb_release -a
# Must show: Ubuntu 22.04
```

If you're on 20.04, use ROS 2 Galactic instead:
```bash
# Replace 'humble' with 'galactic' in all commands
sudo apt install ros-galactic-desktop -y
source /opt/ros/galactic/setup.bash
```

---

## ❌ `ros2: command not found` after installing

**Cause:** ROS 2 not sourced.

**Fix:**
```bash
source /opt/ros/humble/setup.bash
ros2 --version   # Should work now

# Make permanent
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## ❌ GPG key error during `apt update`

```
The following signatures couldn't be verified because the public key is not available
```

**Fix:**
```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
sudo apt update
```

---

## ❌ Locale errors during install

```
locale: Cannot set LC_ALL to default locale
```

**Fix:**
```bash
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
source /etc/default/locale
```
