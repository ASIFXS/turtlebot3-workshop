# STEP 5 — Set Environment Variables

> ⚠️ **Got an error in this step?** → See [ERR_5_env_variables.md](../errors/ERR_5_env_variables.md)

> 📝 **This is the most common cause of failures.** Wrong or missing env vars cause:
> - Gazebo plugin not found errors
> - Robot not spawning
> - Empty/black Gazebo worlds
> - `TURTLEBOT3_MODEL` not set errors

---

## 5.1 — Open Your ~/.bashrc

```bash
nano ~/.bashrc
```

Scroll to the very bottom and **replace or add** the TurtleBot3 section.

---

## 5.2 — The Complete ~/.bashrc Block (Copy This Exactly)

```bash
# ═══════════════════════════════════════════════════
# ROS 2 Humble
# ═══════════════════════════════════════════════════
source /opt/ros/humble/setup.bash

# ═══════════════════════════════════════════════════
# TurtleBot3 Workspace (built from source)
# ═══════════════════════════════════════════════════
source ~/turtlebot3_ws/install/setup.bash

# ═══════════════════════════════════════════════════
# TurtleBot3 Model
# Options: burger | waffle | waffle_pi
# ═══════════════════════════════════════════════════
export TURTLEBOT3_MODEL=burger

# ═══════════════════════════════════════════════════
# Gazebo Plugin Path
# ═══════════════════════════════════════════════════
export GAZEBO_PLUGIN_PATH=/opt/ros/humble/lib

# ═══════════════════════════════════════════════════
# Gazebo Model Path
# ═══════════════════════════════════════════════════
export GAZEBO_MODEL_PATH=~/turtlebot3_ws/src/turtlebot3/turtlebot3_simulations/turtlebot3_gazebo/models

# ═══════════════════════════════════════════════════
# Software Rendering — ONLY enable if Gazebo shows
# a black screen or you are running in a VM
# ═══════════════════════════════════════════════════
# export LIBGL_ALWAYS_SOFTWARE=1
```

Save: `Ctrl+O` → Enter → `Ctrl+X`

---

## 5.3 — Apply Changes

```bash
source ~/.bashrc
```

---

## 5.4 — Verify All Variables

```bash
echo $ROS_DISTRO
# Expected: humble

echo $TURTLEBOT3_MODEL
# Expected: burger

echo $GAZEBO_PLUGIN_PATH
# Expected: /opt/ros/humble/lib

echo $GAZEBO_MODEL_PATH
# Expected: /home/YOUR_USERNAME/turtlebot3_ws/src/...

# Verify the plugin file actually exists
ls /opt/ros/humble/lib/libgazebo_ros_factory.so
# Expected: file path printed (no "No such file" error)
```

---

## 5.5 — Important: Remove Dead Workspace Sources

If you have old/missing workspaces referenced in `~/.bashrc`, remove them.

Common example from your session:
```
not found: "/home/asifali/realsense_ws/install/local_setup.bash"
```

Fix:
```bash
nano ~/.bashrc
# Find and DELETE or comment out any line like:
# source ~/realsense_ws/install/local_setup.bash
# source ~/some_old_ws/install/setup.bash
```

---

## ✅ Checklist Before Moving On

- [ ] `echo $ROS_DISTRO` → `humble`
- [ ] `echo $TURTLEBOT3_MODEL` → `burger`
- [ ] `echo $GAZEBO_PLUGIN_PATH` → `/opt/ros/humble/lib`
- [ ] No "not found" errors when opening a new terminal
- [ ] No duplicate paths (run `echo $GAZEBO_PLUGIN_PATH` — should NOT show the path twice)

➡️ **Next:** [STEP_6_run_simulation.md](STEP_6_run_simulation.md)
