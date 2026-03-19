# STEP 6 — Run the TurtleBot3 Simulation

> ⚠️ **Got an error in this step?** → See [ERR_6_simulation.md](../errors/ERR_6_simulation.md)

---

## 6.1 — Kill Any Existing Gazebo Processes First

Always do this before launching. Old stuck processes cause silent failures.

```bash
killall -9 gzserver gzclient gazebo 2>/dev/null; echo "Gazebo cleared"
ps aux | grep gz | grep -v grep
# Should show nothing (or only the grep itself)
```

---

## 6.2 — Terminal 1: Launch Gazebo World

```bash
source ~/.bashrc
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### ✅ Expected Success Output:
```
[gzserver-1] process started with pid [XXXXX]
[gzclient-2] process started with pid [XXXXX]
[robot_state_publisher-3] got segment base_link
[robot_state_publisher-3] got segment base_footprint
[spawn_entity.py-4] Spawn status: SpawnEntity: Successfully spawned entity [burger]
[turtlebot3_diff_drive] Subscribed to [/cmd_vel]
[turtlebot3_diff_drive] Advertise odometry on [/odom]
```

When you see `Successfully spawned entity [burger]` — the robot is in the world.

---

## 6.3 — Terminal 2: Teleop (Drive the Robot)

Open a **new terminal**:

```bash
source ~/.bashrc
ros2 run turtlebot3_teleop teleop_keyboard
```

### Controls:
```
        w
   a    s    d
        x

w/x : increase/decrease linear velocity
a/d : increase/decrease angular velocity
space key, s : force stop
```

---

## 6.4 — Terminal 3: Visualize in RViz2

Open a **new terminal**:

```bash
source ~/.bashrc
rviz2
```

In RViz2, add these displays:

| Display | Topic | Reliability |
|---------|-------|-------------|
| TF | — | — |
| LaserScan | `/scan` | Best Effort |
| Odometry | `/odom` | — |

Set **Fixed Frame** to `odom`.

---

## 6.5 — Available Worlds

```bash
# Standard obstacle course world
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# House environment (from Medium series - waffle_pi used here)
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py

# Empty world (good for testing)
ros2 launch turtlebot3_gazebo turtlebot3_empty_world.launch.py
```

---

## 6.6 — Useful Debug Commands

```bash
# Check what topics are available
ros2 topic list

# Check if robot is publishing odometry
ros2 topic echo /odom

# Check TF tree
ros2 run tf2_tools view_frames
# Opens frames.pdf in current directory

# Check running nodes
ros2 node list
```

---

## ✅ Checklist Before Moving On

- [ ] Gazebo opens with the TurtleBot3 burger visible
- [ ] `Successfully spawned entity [burger]` appears in terminal
- [ ] `ros2 topic list` shows `/cmd_vel`, `/odom`, `/scan`
- [ ] Teleop moves the robot in Gazebo

➡️ **Next:** [STEP_7_slam_mapping.md](STEP_7_slam_mapping.md)
