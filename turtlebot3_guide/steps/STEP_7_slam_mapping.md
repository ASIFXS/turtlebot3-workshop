# STEP 7 — SLAM Mapping with Cartographer

> ⚠️ **Got an error in this step?** → See [ERR_7_slam.md](../errors/ERR_7_slam.md)

> 📝 **Note (Galactic → Humble):** The Medium series uses `slam_toolbox`.
> For Humble with TurtleBot3, **Cartographer** works more reliably out of the box.
> Both work — Cartographer steps are below, slam_toolbox alternative at the bottom.

---



---

## 7.2 — Terminal 1: Launch Gazebo Simulation

```bash
source ~/.bashrc
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Wait for `Successfully spawned entity [burger]` before continuing.

---

## 7.3 — Terminal 2: Launch SLAM (slamtoolbox)

Open a **new terminal**:

```bash
source ~/.bashrc
ros2 launch slam_toolbox online_async_launch.py
```


```bash
source ~/.bashrc
ros2 run turtlebot3_teleop teleop_keyboard
```

This opens **RViz2 automatically** with the map display.

> ⚠️ Always pass `use_sim_time:=True` when using simulation — without this, the map will not update correctly.

---

## 7.4 — Terminal 3: Drive the Robot to Build the Map

Open a **new terminal**:

```bash
source ~/.bashrc
ros2 run turtlebot3_teleop teleop_keyboard
```

Drive the robot slowly around the entire world.
Watch the map fill in on RViz2 as you explore.

Tips for a good map:
- Drive slowly
- Cover all areas including behind obstacles
- Revisit areas for better accuracy
- Avoid fast turns

---

## 7.5 — Terminal 4: Save the Map

When the map looks complete, open a **new terminal**:

```bash
source ~/.bashrc
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```

This saves two files in your home directory:
```
~/my_map.pgm    ← The map image (grey = free, black = wall, grey border = unknown)
~/my_map.yaml   ← Map metadata (resolution, origin)
```

Verify:
```bash
ls ~/my_map*
# Should show: /home/USERNAME/my_map.pgm  /home/USERNAME/my_map.yaml
```

---

## 7.6 — Alternative: slam_toolbox (from Medium series)

If you prefer slam_toolbox:

```bash
sudo apt install ros-humble-slam-toolbox -y

# Launch (instead of cartographer)
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
```

---

## ✅ Checklist Before Moving On

- [ ] Cartographer launched without errors
- [ ] Map builds in RViz2 as you drive
- [ ] Map saved: `~/my_map.pgm` and `~/my_map.yaml` both exist
- [ ] Map covers the full world area

➡️ **Next:** [STEP_8_navigation_nav2.md](STEP_8_navigation_nav2.md)
