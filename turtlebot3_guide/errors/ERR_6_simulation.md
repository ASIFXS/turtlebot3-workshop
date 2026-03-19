# ERR 6 — Errors During Simulation Launch (Gazebo / Robot)

> ← Back to [STEP_6_run_simulation.md](../steps/STEP_6_run_simulation.md)

---

## ❌ Gazebo opens but shows a BLACK SCREEN / empty world

This is the most common issue. Try these fixes in order:

### Fix A — Enable Software Rendering (VM / no GPU)
```bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

To make permanent, add to `~/.bashrc`:
```bash
echo "export LIBGL_ALWAYS_SOFTWARE=1" >> ~/.bashrc
source ~/.bashrc
```

### Fix B — Update GPU Drivers
```bash
sudo ubuntu-drivers autoinstall
sudo reboot
```

### Fix C — Run Gazebo in Verbose Mode to See Exact Error
```bash
gazebo --verbose
```

### Fix D — Check OpenGL
```bash
glxinfo | grep "OpenGL version"
# If glxinfo not found:
sudo apt install mesa-utils -y
glxinfo | grep "OpenGL version"
```

---

## ❌ `[gzclient-2] process has died` — Gazebo window crashes immediately

**Cause:** GPU/display driver issue.

**Fix:**
```bash
export LIBGL_ALWAYS_SOFTWARE=1
# Then relaunch
```

---

## ❌ `spawn_entity.py` hangs waiting for `/spawn_entity` service (timeout)

```
[spawn_entity.py-4] Waiting for service /spawn_entity, timeout = 30
```

**Cause:** `gzserver` is not fully started yet, or a previous instance is blocking.

**Fix:**
```bash
# Kill all existing Gazebo processes
killall -9 gzserver gzclient gazebo 2>/dev/null

# Wait a moment
sleep 3

# Check nothing is running
ps aux | grep gz | grep -v grep   # Should show nothing

# Relaunch
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

## ❌ "Was Gazebo started with GazeboRosFactory?" error

**Cause:** A gzserver is already running from a previous session.

**Fix:**
```bash
killall -9 gzserver gzclient
# Wait a few seconds, then relaunch
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

## ❌ Robot spawns but does NOT appear in the Gazebo window

**Cause:** gzclient (the visual window) and gzserver (the physics) are out of sync.

**Fix:**
```bash
# Kill and restart everything
killall -9 gzserver gzclient
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

## ❌ `TURTLEBOT3_MODEL` not set — launch fails immediately

```
[ERROR] TURTLEBOT3_MODEL is not set
```

**Fix:**
```bash
export TURTLEBOT3_MODEL=burger
# Add to ~/.bashrc permanently:
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

---

## ❌ `ros2 run turtlebot3_teleop teleop_keyboard` — package not found

**Fix:**
```bash
sudo apt install ros-humble-turtlebot3 -y
source ~/.bashrc
```

---

## ❌ Teleop keyboard runs but robot doesn't move in Gazebo

**Diagnose:**
```bash
# Check /cmd_vel topic is being published when you press keys
ros2 topic echo /cmd_vel

# Check robot is subscribed to cmd_vel
ros2 topic info /cmd_vel
```

**Common Causes:**
- Gazebo simulation is paused — click the Play button in Gazebo
- Wrong terminal sourcing — make sure both terminals sourced `~/.bashrc`
- `TURTLEBOT3_MODEL` mismatch between terminals

---

## ❌ RViz2 shows no LaserScan data

**Fix:**
1. In RViz2 → LaserScan display → change **Reliability Policy** to `Best Effort`
2. Confirm topic is `/scan`: `ros2 topic list | grep scan`

---

## ❌ `ros2 run tf2_tools view_frames` — no output / error

```bash
sudo apt install ros-humble-tf2-tools -y
ros2 run tf2_tools view_frames
# Check for frames.pdf in current directory
evince frames.pdf   # or: xdg-open frames.pdf
```
