# 🤖 TurtleBot3 Simulation — Complete Setup Guide (From Scratch)
> **System:** Ubuntu 22.04 | **ROS:** Humble | **Gazebo:** Classic 11  
> Based on real troubleshooting session — includes all common fixes

---

## 📋 Table of Contents
1. [Clean Up Old Gazebo (MUST DO FIRST)](#-step-1--clean-up-old-gazebo)
2. [Install ROS 2 Humble](#-step-2--install-ros-2-humble)
3. [Install Gazebo Classic 11](#-step-3--install-gazebo-classic-11)
4. [Install TurtleBot3 Packages](#-step-4--install-turtlebot3-packages)
5. [Set Environment Variables](#-step-5--set-environment-variables-critical)
6. [Build Your Workspace](#-step-6--build-the-workspace)
7. [Run the Simulation](#-step-7--run-the-simulation)
8. [Gazebo Not Loading? Fix It Here](#-gazebo-not-loading--black-screen-fixes)
9. [SLAM — Autonomous Mapping](#-step-8--slam-mapping)
10. [Navigation (Nav2)](#-step-9--navigation-nav2)
11. [Common Errors & Fixes](#-common-errors--fixes)
12. [Quick Command Reference](#-quick-command-reference)

---

## 🧹 STEP 1 — Clean Up Old Gazebo

> ⚠️ **Skip nothing here.** Leftover Gazebo installs cause 90% of simulation problems.

```bash
# Remove all Gazebo versions
sudo apt remove --purge '*gazebo*' -y
sudo apt remove --purge '*ignition*' -y

# Remove old ROS Gazebo bindings
sudo apt remove --purge 'ros-*gazebo*' -y

# Clean up leftover dependencies
sudo apt autoremove -y
sudo apt autoclean

# Verify nothing is left
dpkg -l | grep -i gazebo   # Should return NOTHING
```

---

## 🔧 STEP 2 — Install ROS 2 Humble

```bash
# Set locale
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Add ROS 2 apt repository
sudo apt install software-properties-common curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
  http://packages.ros.org/ros2/ubuntu \
  $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS 2 Humble Desktop
sudo apt update
sudo apt install ros-humble-desktop -y

# Install build tools
sudo apt install python3-colcon-common-extensions python3-rosdep -y
```

---

## 🌐 STEP 3 — Install Gazebo Classic 11

> Use **Gazebo Classic 11** — NOT Gazebo Fortress/Garden/Harmonic (those are Ignition-based and incompatible with TurtleBot3 packages).

```bash
sudo apt install gazebo -y
sudo apt install ros-humble-gazebo-ros-pkgs -y
sudo apt install ros-humble-gazebo-ros2-control -y

# Verify version (must show Gazebo 11.x)
gazebo --version
```

---

## 📦 STEP 4 — Install TurtleBot3 Packages

```bash
sudo apt install \
  ros-humble-turtlebot3 \
  ros-humble-turtlebot3-simulations \
  ros-humble-turtlebot3-gazebo \
  ros-humble-turtlebot3-msgs \
  ros-humble-dynamixel-sdk \
  -y
```

---

## ⚙️ STEP 5 — Set Environment Variables (CRITICAL)

> These **must** be in your `~/.bashrc`. Without them, Gazebo plugins fail silently.

```bash
# Open bashrc
nano ~/.bashrc
```

Add ALL of these lines at the bottom:

```bash
# ── ROS 2 Humble ──────────────────────────────────────────────
source /opt/ros/humble/setup.bash

# ── TurtleBot3 Workspace (if you built one) ───────────────────
# source ~/turtlebot3_ws/install/setup.bash

# ── TurtleBot3 Model (choose: burger / waffle / waffle_pi) ────
export TURTLEBOT3_MODEL=burger

# ── Gazebo Plugin Path ─────────────────────────────────────────
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib:$GAZEBO_PLUGIN_PATH

# ── Gazebo Model Path ──────────────────────────────────────────
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models

# ── Software Rendering (use ONLY if Gazebo shows black screen) ─
# export LIBGL_ALWAYS_SOFTWARE=1
```

Apply changes:
```bash
source ~/.bashrc
```

Verify the plugin path is set:
```bash
echo $GAZEBO_PLUGIN_PATH
# Should output: /opt/ros/humble/lib:
```

---

## 🔨 STEP 6 — Build the Workspace

> Only needed if you cloned source packages. Skip if using apt-installed packages only.

```bash
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws/src

# Clone TurtleBot3 packages
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git

cd ~/turtlebot3_ws

# Initialize rosdep (first time only)
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -r -y

# Build
colcon build --symlink-install

# Source the workspace
source ~/turtlebot3_ws/install/setup.bash
```

Add to `~/.bashrc`:
```bash
echo "source ~/turtlebot3_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## 🚀 STEP 7 — Run the Simulation

### Terminal 1 — Launch Gazebo World
```bash
source ~/.bashrc
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

✅ **Expected output (success signs):**
```
[gzserver-1] process started with pid [XXXXX]
[gzclient-2] process started with pid [XXXXX]
[robot_state_publisher-3] got segment base_link
[spawn_entity.py-4] Spawn status: SpawnEntity: Successfully spawned entity [burger]
[turtlebot3_diff_drive] Subscribed to [/cmd_vel]
[turtlebot3_diff_drive] Advertise odometry on [/odom]
```

### Terminal 2 — Teleoperate the Robot
```bash
source ~/.bashrc
ros2 run turtlebot3_teleop teleop_keyboard
```

| Key | Action |
|-----|--------|
| `W` | Move Forward |
| `S` | Move Backward |
| `A` | Turn Left |
| `D` | Turn Right |
| `Space` | Stop |

---

## 🖥️ Gazebo Not Loading / Black Screen Fixes

> These are the most common issues. Try them in order.

### Fix 1 — Software Rendering (VM / No GPU)
```bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

To make it permanent, uncomment this line in `~/.bashrc`:
```bash
export LIBGL_ALWAYS_SOFTWARE=1
```

### Fix 2 — Kill Stuck Gazebo Processes
```bash
# Check for lingering processes
ps aux | grep gz

# Kill them all
killall -9 gzserver gzclient gazebo

# Verify they are gone
ps aux | grep gz  # Should only show the grep itself
```

### Fix 3 — Plugin Path Not Set
```bash
# Check if plugin path is set
echo $GAZEBO_PLUGIN_PATH

# If empty, set it manually
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib:$GAZEBO_PLUGIN_PATH

# Verify the library exists
ls /opt/ros/humble/lib/libgazebo_ros_factory.so
```

### Fix 4 — Run Gazebo in Verbose Mode (to see exact error)
```bash
gazebo --verbose
```

### Fix 5 — Missing RealSense Workspace Error
If you see:
```
not found: "/home/asifali/realsense_ws/install/local_setup.bash"
```
This means your `~/.bashrc` has a reference to a workspace that doesn't exist. Fix it:
```bash
nano ~/.bashrc
# Find and DELETE or COMMENT OUT this line:
# source ~/realsense_ws/install/local_setup.bash
source ~/.bashrc
```

### Fix 6 — Gazebo Opens But Robot Doesn't Appear
```bash
# Check if spawn service is running
ros2 service list | grep spawn

# Manually re-spawn the robot
ros2 run gazebo_ros spawn_entity.py \
  -file /opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf \
  -entity burger
```

### Fix 7 — Double Plugin Path (shows /opt/ros/humble/lib:/opt/ros/humble/lib:)
Your `~/.bashrc` is appending on top of itself. Fix:
```bash
nano ~/.bashrc
# Change this:
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib:$GAZEBO_PLUGIN_PATH
# To this (set it once, cleanly):
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib
```
Then:
```bash
source ~/.bashrc
echo $GAZEBO_PLUGIN_PATH   # Should show: /opt/ros/humble/lib
```

---

## 🗺️ STEP 8 — SLAM Mapping

### Install Cartographer
```bash
sudo apt install \
  ros-humble-cartographer \
  ros-humble-cartographer-ros \
  -y
```

### Terminal 1 — Gazebo Simulation
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Terminal 2 — Launch SLAM
```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```

### Terminal 3 — Drive the Robot
```bash
ros2 run turtlebot3_teleop teleop_keyboard
```
Drive around to fill in the map in RViz2.

### Terminal 4 — Save the Map
```bash
ros2 run nav2_map_server map_saver_cli -f ~/my_map
# Creates: ~/my_map.pgm and ~/my_map.yaml
```

---

## 🧭 STEP 9 — Navigation (Nav2)

### Install Nav2
```bash
sudo apt install \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  -y
```

### Terminal 1 — Gazebo Simulation
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Terminal 2 — Nav2 with Saved Map
```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=True \
  map:=$HOME/my_map.yaml
```

In **RViz2**:
1. Click **"2D Pose Estimate"** → click on the map where the robot IS
2. Click **"Nav2 Goal"** → click where you want the robot to GO
3. Watch it navigate autonomously! 🎉

---

## 🔴 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `not found: .../realsense_ws/...` | Old workspace sourced in bashrc | Remove that line from `~/.bashrc` |
| Gazebo opens, black/empty world | No GPU / software rendering off | `export LIBGL_ALWAYS_SOFTWARE=1` |
| `GAZEBO_PLUGIN_PATH` is empty | Not set in bashrc | Add export line, then `source ~/.bashrc` |
| Double path in `GAZEBO_PLUGIN_PATH` | Bashrc sourced multiple times | Set the variable once without `$GAZEBO_PLUGIN_PATH` at end |
| `spawn_entity` hangs / timeout | gzserver not fully started | Wait 10–15s; check `ps aux | grep gz` |
| `package not found` for turtlebot3 | Package not installed | `sudo apt install ros-humble-turtlebot3*` |
| Robot spawns but doesn't move | `cmd_vel` topic mismatch | Check: `ros2 topic list | grep cmd_vel` |
| SLAM map all black | `use_sim_time` not set | Always pass `use_sim_time:=True` |
| `colcon build` fails | Missing deps | Run `rosdep install --from-paths src --ignore-src -r -y` first |

---

## ⚡ Quick Command Reference

```bash
# ── Environment Setup ────────────────────────────────────────────
source /opt/ros/humble/setup.bash
source ~/turtlebot3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib

# ── Kill stuck Gazebo ────────────────────────────────────────────
killall -9 gzserver gzclient gazebo

# ── Check running processes ──────────────────────────────────────
ps aux | grep gz

# ── Launch simulation ────────────────────────────────────────────
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# ── Available worlds ─────────────────────────────────────────────
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py      # Obstacle course
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py      # House environment
ros2 launch turtlebot3_gazebo turtlebot3_empty_world.launch.py  # Empty world

# ── Teleop ───────────────────────────────────────────────────────
ros2 run turtlebot3_teleop teleop_keyboard

# ── SLAM ─────────────────────────────────────────────────────────
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True

# ── Save map ─────────────────────────────────────────────────────
ros2 run nav2_map_server map_saver_cli -f ~/my_map

# ── Navigation ───────────────────────────────────────────────────
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/my_map.yaml

# ── Debug plugin path ────────────────────────────────────────────
echo $GAZEBO_PLUGIN_PATH
ls /opt/ros/humble/lib/libgazebo_ros_factory.so

# ── Software rendering (for VM/no GPU) ───────────────────────────
export LIBGL_ALWAYS_SOFTWARE=1
```

---

## ✅ Verified Working ~/.bashrc (Copy This Exactly)

```bash
# ROS 2 Humble
source /opt/ros/humble/setup.bash

# TurtleBot3 Workspace (uncomment if you built from source)
# source ~/turtlebot3_ws/install/setup.bash

# TurtleBot3 Model
export TURTLEBOT3_MODEL=burger

# Gazebo Paths
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib
export GAZEBO_MODEL_PATH=/opt/ros/humble/share/turtlebot3_gazebo/models

# Uncomment the line below ONLY if Gazebo shows black screen (VM/no GPU)
# export LIBGL_ALWAYS_SOFTWARE=1
```

---

*Guide built from real troubleshooting session on Ubuntu 22.04 + ROS 2 Humble + Gazebo Classic 11*  
*Last updated: March 2026*
