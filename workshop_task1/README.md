# 🤖 Workshop — TurtleBot3 ROS 2 Tasks
> ROS 2 Humble | Ubuntu 22.04 | TurtleBot3 Burger

---

## 📁 Structure

```
workshop_task1/
├── CMakeLists.txt
├── package.xml
└── workshop_task1/
    ├── __init__.py
    ├── move_robot.py
    ├── draw_circle.py
    └── navigate_to_goal.py
```

---

## 🔨 Build

```bash
cd ~/turtlebot3_ws
colcon build --symlink-install \
  --cmake-args -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  --packages-select workshop_task1
source ~/turtlebot3_ws/install/setup.bash
```

---

## 📌 Task 1 — Drive to a Goal

**Fill in:** `calculate_distance()` and `drive_forward()`

```bash
# Terminal 1
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# Terminal 2
ros2 run workshop_task1 move_robot.py
```

✅ Robot drives straight and stops at `GOAL_DISTANCE` metres.

---

## 📌 Task 2 — Draw a Circle

**Fill in:** `ANGULAR_SPEED`, `publisher`, and `drive()`

```bash
# Terminal 1
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# Terminal 2
ros2 run workshop_task1 draw_circle.py
```

✅ Robot drives in a circle. Press `Ctrl+C` to stop.

> 💡 `radius = LINEAR_SPEED / ANGULAR_SPEED`

---

## 📌 Task 3 — Navigate to a Goal with Nav2

### Step 1 — Launch Gazebo

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Step 2 — Launch Nav2

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=True \
  map:=$HOME/map.yaml
```

### Step 3 — Set robot pose in RViz2

- Click **"2D Pose Estimate"** → click where the robot is on the map
- Wait for green particle cloud ✅

### Step 4 — Find your goal coordinates

- Click **"Publish Point"** in RViz2 → click your goal on the map
- Run in a new terminal to see the coordinates:

```bash
ros2 topic echo /clicked_point --once
```

> `frame_id: map` confirms these are map coordinates ✅

### Step 5 — Fill in your coordinates

Open `navigate_to_goal.py` and fill in TODO 1:

```python
GOAL_X = 0.0   # ← your X from Publish Point
GOAL_Y = 0.0   # ← your Y from Publish Point
```

### Step 6 — Fill in TODOs 2, 3, 4 then run

```bash
ros2 run workshop_task1 navigate_to_goal.py
```

✅ Expected output:
```
Sending goal...
Moving...
Remaining: x.xx m
=== GOAL REACHED! ===
```
