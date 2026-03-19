# STEP 4 — Install Gazebo & Build the Workspace

> ⚠️ **Got an error in this step?** → See [ERR_4_gazebo_build.md](../errors/ERR_4_gazebo_build.md)

> 📝 **Important:** Use **Gazebo Classic 11** — NOT Gazebo Fortress, Garden, or Harmonic.
> Those are Ignition-based and NOT compatible with TurtleBot3 on Humble.

---

## 4.1 — Install Gazebo Classic 11

```bash
sudo apt install gazebo -y
sudo apt install ros-humble-gazebo-ros-pkgs -y
sudo apt install ros-humble-gazebo-ros2-control -y
```

Verify version:
```bash
gazebo --version
# Must show: Gazebo 11.X.X
```

---

## 4.2 — Install Dependencies with rosdep

```bash
cd ~/turtlebot3_ws
source /opt/ros/humble/setup.bash

rosdep install --from-paths src --ignore-src -r -y
```

This reads all packages in `src/` and installs missing system dependencies automatically.

---

## 4.3 — Build the Workspace

```bash
cd ~/turtlebot3_ws
source /opt/ros/humble/setup.bash

colcon build --symlink-install
```

Expected output (success):
```
Summary: X packages finished [Xs]
  X packages had stderr output: ...
```

> ⏱️ First build takes 3–10 minutes depending on your machine.

If you see `0 packages failed` — you are good.

---

## 4.4 — Source the Built Workspace

```bash
source ~/turtlebot3_ws/install/setup.bash
```

Add to `~/.bashrc` permanently:
```bash
echo "source ~/turtlebot3_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Verify packages are found:
```bash
ros2 pkg list | grep turtlebot3
# Should list: turtlebot3_gazebo, turtlebot3_bringup, etc.
```

---

## ✅ Checklist Before Moving On

- [ ] `gazebo --version` shows Gazebo 11.X.X
- [ ] `colcon build` finished with `0 packages failed`
- [ ] `ros2 pkg list | grep turtlebot3` shows packages
- [ ] `source ~/turtlebot3_ws/install/setup.bash` is in `~/.bashrc`

➡️ **Next:** [STEP_5_env_variables.md](STEP_5_env_variables.md)
