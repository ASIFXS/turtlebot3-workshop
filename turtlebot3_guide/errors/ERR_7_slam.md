# ERR 7 — Errors During SLAM Mapping

> ← Back to [STEP_7_slam_mapping.md](../steps/STEP_7_slam_mapping.md)

---

## ❌ Map not updating in RViz2 — stays blank/grey

**Cause 1:** `use_sim_time:=True` was not passed.

**Fix:**
```bash
# Always use this flag with simulation
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```

**Cause 2:** Robot is not publishing `/scan` topic.

**Diagnose:**
```bash
ros2 topic list | grep scan
ros2 topic echo /scan   # Should see data flowing when Gazebo is running
```

---

## ❌ `ros2 launch turtlebot3_cartographer` — package not found

**Fix:**
```bash
sudo apt install ros-humble-cartographer ros-humble-cartographer-ros -y
source ~/.bashrc

# If still not found — check if it's in turtlebot3_ws:
ros2 pkg list | grep cartographer
```

---

## ❌ Cartographer crashes immediately with transform error

```
Could not find a connection between 'map' and 'base_footprint'
```

**Cause:** Robot not publishing TF transforms — Gazebo may not be running or robot not spawned.

**Fix:**
```bash
# Make sure Gazebo is running and robot is spawned FIRST
# Then launch cartographer in a new terminal
ros2 topic list | grep /scan    # Confirm scan is being published
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```

---

## ❌ `map_saver_cli` fails — service not available

```
[map_saver-1] [WARN] Waiting for service /map_saver/save_map
```

**Cause:** `nav2_map_server` not installed.

**Fix:**
```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup -y
source ~/.bashrc
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```

---

## ❌ Map saves but `my_map.pgm` is all black

**Cause 1:** Robot was not moved around — map has no explored area.
Drive the robot around more with teleop.

**Cause 2:** Wrong `use_sim_time` setting caused time mismatch.
```bash
# Kill cartographer, relaunch with:
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```

---

## ❌ slam_toolbox alternative fails

```
[slam_toolbox] No laser scan received
```

**Fix:**
```bash
# Confirm scan topic exists
ros2 topic list | grep scan

# Relaunch with correct params
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
```

---

## ❌ RViz2 crashes when cartographer launches

**Cause:** GPU/display issue.

**Fix:**
```bash
export LIBGL_ALWAYS_SOFTWARE=1
# Relaunch everything
```
