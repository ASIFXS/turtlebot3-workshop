# STEP 8 — Autonomous Navigation with Nav2

> ⚠️ **Got an error in this step?** → See [ERR_8_navigation.md](../errors/ERR_8_navigation.md)

> 📝 **Note (Galactic → Humble):** The Medium series uses `nav2_bringup bringup_launch.py`.
> For Humble + TurtleBot3, use `turtlebot3_navigation2 navigation2.launch.py` — it handles
> all TurtleBot3-specific configs automatically.

---

## 8.0 — Prerequisites

Before starting:
- [ ] You completed STEP 7 and have `~/my_map.pgm` and `~/my_map.yaml`
- [ ] Kill slam_toolbox/cartographer and teleop from Step 7
- [ ] Only the Gazebo simulation should be running

---

## 8.1 — Install Nav2

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup -y
```

---

## 8.2 — Terminal 1: Launch Gazebo Simulation

```bash
source ~/.bashrc
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

## 8.3 — Terminal 2: Launch Nav2 with Your Map

Open a **new terminal**:

```bash
source ~/.bashrc
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=True \
  map:=$HOME/my_map.yaml
```

This launches:
- `amcl` — localization (provides `map → odom` transform)
- `nav2_planner` — global path planning
- `nav2_controller` — local path following
- `nav2_bt_navigator` — behavior tree navigation
- RViz2 with Nav2 default view

---

## 8.4 — Set Initial Pose in RViz2

Nav2 needs to know where the robot currently is in the map.

1. In RViz2, click **"2D Pose Estimate"** button (top toolbar)
2. Click on the map where the robot **currently is** in Gazebo
3. Hold and drag to set the **heading direction**
4. Release

You should see green arrows appear around the robot — that is `amcl` particle cloud confirming localization.

> ⚠️ If you skip this step, Nav2 will show "Global Status Error" because `amcl` has no initial pose.

---

## 8.5 — Send a Navigation Goal

1. In RViz2, click **"Nav2 Goal"** button (top toolbar)
2. Click a destination on the map
3. Hold and drag to set the **target orientation**
4. Release and watch the robot plan a path and navigate!

You will see:
- A global path (usually green/white line) planned in RViz2
- The robot moving in Gazebo
- Local costmap updating around the robot

---

## 8.6 — Send Goals from Terminal (Optional)

```bash
source ~/.bashrc
ros2 topic pub /goal_pose geometry_msgs/PoseStamped \
  "{header: {frame_id: 'map'}, pose: {position: {x: 1.0, y: 0.5, z: 0.0}, orientation: {w: 1.0}}}"
```

---

## 8.7 — Understanding What Nav2 Needs (from Medium series)

As the article explains:

| Need | What provides it | ROS topic/TF |
|------|-----------------|--------------|
| Robot location | `amcl` (localization) | `map → odom` TF |
| Local motion | Wheel encoders | `odom → base_link` TF |
| Map | `map_server` | `/map` topic |

The full TF chain for navigation: `map → odom → base_link`

---

## ✅ Final Checklist

- [ ] Nav2 launches without fatal errors
- [ ] RViz2 shows the map loaded
- [ ] Initial pose set with "2D Pose Estimate"
- [ ] Robot navigates to goals set with "Nav2 Goal"
- [ ] `ros2 topic list` shows `/amcl_pose`, `/plan`, `/cmd_vel`

---

## 🎉 You're Done!

Full pipeline working:
```
Gazebo Simulation
      ↓
  TurtleBot3 Burger
      ↓
   SLAM Mapping    →   Saved Map
      ↓
  Nav2 Navigation  ←   Saved Map
      ↓
  Autonomous Robot!
```
