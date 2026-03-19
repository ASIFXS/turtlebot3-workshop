# ERR 8 — Errors During Nav2 Navigation

> ← Back to [STEP_8_navigation_nav2.md](../steps/STEP_8_navigation_nav2.md)

---

## ❌ "Global Status: Error" in RViz2 after Nav2 launches

**Cause:** `amcl` has no initial pose — it doesn't know where the robot is in the map.

**Fix:**
1. In RViz2, click **"2D Pose Estimate"** in the top toolbar
2. Click the map at the robot's current position in Gazebo
3. Drag to set the heading direction
4. Release — you'll see green arrows (particle cloud) appear

This provides `amcl` with the initial pose and resolves the `map → odom` TF.

---

## ❌ Map not showing in RViz2 after Nav2 launch

**Cause 1:** Map file path is wrong.

**Fix:**
```bash
# Verify the map file exists
ls ~/my_map.yaml
ls ~/my_map.pgm

# Relaunch with full path
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=True \
  map:=$HOME/my_map.yaml
```

**Cause 2:** Map was saved with wrong format.

**Check:**
```bash
cat ~/my_map.yaml
# Should show image, resolution, origin, negate, occupied_thresh, free_thresh
```

---

## ❌ Nav2 launches but robot doesn't move toward goal

**Cause 1:** Initial pose not set — set "2D Pose Estimate" first.

**Cause 2:** Nav2 is still initialising — wait ~10 seconds after launch.

**Cause 3:** Goal is inside a wall/obstacle on the map.

**Diagnose:**
```bash
# Check if /cmd_vel is being published
ros2 topic echo /cmd_vel

# Check nav2 action server status
ros2 action list
# Should include: /navigate_to_pose
```

---

## ❌ `amcl` not finding correct position — robot drifts

**Cause:** Initial pose estimate was too far from actual robot position.

**Fix:**
1. In Gazebo, note the exact robot position (X, Y coordinates shown in bottom bar)
2. In RViz2, use "2D Pose Estimate" and be more precise
3. Drive the robot with teleop for a short while — `amcl` will converge

---

## ❌ Nav2 crashes with `use_sim_time` warning

```
[amcl] use_sim_time is set but /clock topic not available
```

**Cause:** Gazebo is not publishing the `/clock` topic.

**Fix:**
```bash
# Confirm /clock is published
ros2 topic list | grep clock
# Should show: /clock

# If missing, your gazebo_ros plugin may be broken — rebuild:
cd ~/turtlebot3_ws
colcon build --symlink-install --packages-select turtlebot3_gazebo
source ~/turtlebot3_ws/install/setup.bash
```

---

## ❌ `ros2 launch turtlebot3_navigation2 navigation2.launch.py` — package not found

**Fix:**
```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup -y
source ~/.bashrc

# Also check workspace:
ros2 pkg list | grep navigation2
```

---

## ❌ Robot gets stuck and never reaches goal

**Cause:** Local costmap conflict or poor map quality.

**Quick fixes:**
- Send a new goal closer to the robot
- Check the map quality — was the map fully explored in SLAM?
- Increase recovery behaviour wait time (advanced)

**Restart Nav2 cleanly:**
```bash
# Kill nav2, re-source, relaunch
Ctrl+C  (in nav2 terminal)
source ~/.bashrc
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=True map:=$HOME/my_map.yaml
```

---

## ❌ TF Error: `map` frame not found

```
[rviz2] Could not find transform from 'map' to 'base_link'
```

**Cause:** `amcl` hasn't received initial pose yet.

**Fix:** Set the "2D Pose Estimate" in RViz2 (see top of this file).
