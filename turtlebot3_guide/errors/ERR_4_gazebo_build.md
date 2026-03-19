# ERR 4 — Errors During Gazebo Install & colcon Build

> ← Back to [STEP_4_gazebo_build.md](../steps/STEP_4_gazebo_build.md)

---

## ❌ `gazebo --version` shows Gazebo 9 or Gazebo Fortress instead of 11

**Cause:** Wrong Gazebo version installed — possibly from a previous install.

**Fix:**
```bash
# Remove all gazebo
sudo apt remove --purge '*gazebo*' '*ignition*' -y
sudo apt autoremove -y

# Reinstall Gazebo Classic 11 only
sudo apt install gazebo -y
gazebo --version   # Must now show 11.X.X
```

---

## ❌ `Could not find a configuration file for package "ignition-common3-graphics"`

**Cause:** Gazebo version conflict — system has mixed Gazebo/Ignition files.

**Fix:**
```bash
sudo apt remove --purge '*ignition*' -y
sudo apt autoremove -y
sudo apt install gazebo -y
```

---

## ❌ `colcon build` fails — "CMake Error: Could not find a package configuration file"

**Cause:** Missing system dependency not caught by rosdep.

**Fix:**
```bash
cd ~/turtlebot3_ws
rosdep install --from-paths src --ignore-src -r -y
# Then try build again
colcon build --symlink-install
```

---

## ❌ `colcon build` — packages fail but others succeed

Check which package failed:
```bash
cd ~/turtlebot3_ws
colcon build --symlink-install 2>&1 | grep "Failed\|Error"
```

Then build only that package to see full error:
```bash
colcon build --packages-select <failing_package_name>
```

---

## ❌ `colcon build` — DynamixelSDK or hls_lfcd errors

These utility packages sometimes have minor build warnings. If they fail:

```bash
# Try building only the core packages
colcon build --symlink-install \
  --packages-select turtlebot3_msgs turtlebot3_gazebo turtlebot3_bringup \
  turtlebot3_cartographer turtlebot3_navigation2
```

---

## ❌ `ros2 pkg list | grep turtlebot3` shows nothing after build

**Cause:** Workspace not sourced after build.

**Fix:**
```bash
source ~/turtlebot3_ws/install/setup.bash
ros2 pkg list | grep turtlebot3   # Should now show packages
```

Make it permanent:
```bash
echo "source ~/turtlebot3_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## ❌ Build warns about cmake version

The Medium series mentions cmake 3.13.4 works better than 3.2X.X.
On Ubuntu 22.04 with Humble this is usually not an issue, but if you see cmake errors:

```bash
cmake --version
# If very old, update:
sudo apt install cmake -y
```

---

## ❌ `ros-humble-gazebo-ros-pkgs` not found

```bash
sudo apt update
sudo apt install ros-humble-gazebo-ros-pkgs -y

# If still fails, check your ROS repo is set up:
cat /etc/apt/sources.list.d/ros2.list
```
