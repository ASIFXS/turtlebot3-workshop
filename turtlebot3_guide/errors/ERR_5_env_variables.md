# ERR 5 — Errors From Environment Variables

> ← Back to [STEP_5_env_variables.md](../steps/STEP_5_env_variables.md)

---

## ❌ `not found: "/home/USERNAME/realsense_ws/install/local_setup.bash"`

**Cause:** Your `~/.bashrc` sources an old workspace that no longer exists.
This was seen in your real session as:
```
not found: "/home/asifali/realsense_ws/install/local_setup.bash"
```

**Fix:**
```bash
nano ~/.bashrc
# Find and DELETE or comment out the line:
# source ~/realsense_ws/install/local_setup.bash

# Save: Ctrl+O → Enter → Ctrl+X
source ~/.bashrc
```

---

## ❌ `echo $TURTLEBOT3_MODEL` returns empty / blank

**Cause:** The export line is missing from `~/.bashrc` or was not sourced.

**Fix:**
```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
echo $TURTLEBOT3_MODEL   # Should now show: burger
```

---

## ❌ `echo $GAZEBO_PLUGIN_PATH` shows the path TWICE

Example of the problem:
```
/opt/ros/humble/lib:/opt/ros/humble/lib:
```

**Cause:** Your `~/.bashrc` has this line:
```bash
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib:$GAZEBO_PLUGIN_PATH
```
Every time bashrc is sourced, it appends again.

**Fix:**
```bash
nano ~/.bashrc
# Change this:
#   export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib:$GAZEBO_PLUGIN_PATH
# To this (set it cleanly, no self-reference):
#   export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib

source ~/.bashrc
echo $GAZEBO_PLUGIN_PATH   # Should now show exactly: /opt/ros/humble/lib
```

---

## ❌ `echo $GAZEBO_PLUGIN_PATH` is empty even after sourcing bashrc

**Cause:** The export line is missing from `~/.bashrc`.

**Fix:**
```bash
echo "export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib" >> ~/.bashrc
source ~/.bashrc
echo $GAZEBO_PLUGIN_PATH   # Should now show: /opt/ros/humble/lib
```

---

## ❌ `ls /opt/ros/humble/lib/libgazebo_ros_factory.so` — No such file

**Cause:** `ros-humble-gazebo-ros-pkgs` was not installed.

**Fix:**
```bash
sudo apt install ros-humble-gazebo-ros-pkgs -y
ls /opt/ros/humble/lib/libgazebo_ros_factory.so   # Should now exist
```

---

## ❌ Opening a new terminal shows lots of "not found" errors

**Cause:** Multiple broken workspace sources in `~/.bashrc`.

**Diagnose:**
```bash
cat ~/.bashrc | grep "source"
# Look for any paths that don't exist on your system
```

**Fix — check each sourced path:**
```bash
# For each source line found, verify the file exists:
ls /path/shown/in/bashrc/setup.bash

# Delete any source lines pointing to non-existent files
nano ~/.bashrc
```

---

## ❌ `ROS_DISTRO` is not set or shows wrong distro

**Fix:**
```bash
# Check what's in bashrc
grep "ros" ~/.bashrc

# Make sure this line is present and not commented out:
# source /opt/ros/humble/setup.bash

source ~/.bashrc
echo $ROS_DISTRO   # Should show: humble
```
