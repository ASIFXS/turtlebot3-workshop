# 🏎️ Task 1: TurtleBot3 Autorace Simulation & Teleoperation

| Detail | Info |
|--------|------|
| **Target OS** | Ubuntu 22.04 |
| **ROS 2 Version** | Humble Hawksbill |
| **Robot Model** | `burger_cam` |

---

## 📝 Overview

In this task, you will install the **TurtleBot3 Autorace 2020** packages into your existing ROS 2 workspace. You will configure your environment to use the `burger_cam` robot, launch the 3D Autorace track in Gazebo, and use the keyboard teleoperation node to drive the robot around the track.

---

## 🛠️ Step 1: Download the Autorace Packages

Since you already have the standard TurtleBot3 packages in your workspace, you only need to add the Autorace repositories.

1. Open a terminal and navigate to your workspace's `src` folder:

    ```bash
    cd ~/turtlebot3_ws/src
    ```

2. Clone the Autorace 2020 repository for ROS 2:

    ```bash
    git clone -b ros2 https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020.git
    ```

---

## 🏗️ Step 2: Build the Workspace

Now that the new packages are in the `src` folder, compile them.

1. Return to the root of your workspace:

    ```bash
    cd ~/turtlebot3_ws
    ```

2. Build the workspace:

    > **Note:** The `--cmake-args` flags ensure compatibility with newer systems and suppress developer warnings.

    ```bash
    colcon build --symlink-install --cmake-args -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -Wno-dev
    ```

3. Source the freshly built workspace:

    ```bash
    source install/setup.bash
    ```

---

## 🌍 Step 3: Configure Your Environment Variables

Gazebo needs to know where the Autorace 3D models are located, and ROS 2 needs to know which robot model to use.

Run **both** of these commands in your terminal:

```bash
export TURTLEBOT3_MODEL=burger_cam
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/install/turtlebot3_gazebo/share/turtlebot3_gazebo/models
```

> 💡 **Pro-Tip:** To avoid re-typing these every time you open a new terminal, add them to the bottom of your `~/.bashrc` file:
>
> ```bash
> echo 'export TURTLEBOT3_MODEL=burger_cam' >> ~/.bashrc
> echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/install/turtlebot3_gazebo/share/turtlebot3_gazebo/models' >> ~/.bashrc
> source ~/.bashrc
> ```

---

## 🚀 Step 4: Launch the Autorace World in Gazebo

1. Run the Autorace launch file:

    ```bash
    ros2 launch turtlebot3_gazebo turtlebot3_autorace_2020.launch.py
    ```

2. Gazebo should open displaying:
   - A track with black roads and white/yellow lane markings
   - Traffic lights and road signs
   - Your TurtleBot3 spawned in the centre of the track

> ⚠️ **Troubleshooting — Gazebo crashes with exit code 255?**
>
> This happens when a previous Gazebo session didn't close properly and is still running in the background. Open a **new terminal** and run:
>
> ```bash
> killall -9 gzserver gzclient
> ```
>
> Then try launching the world again.

---

## 🎮 Step 5: Drive the Robot (Teleoperation)

Because the terminal from Step 4 is busy running Gazebo, you **must open a new terminal** for this step.

1. Open a **New Terminal** (`Ctrl` + `Alt` + `T`)

2. Source ROS 2 and your workspace:

    ```bash
    source /opt/ros/humble/setup.bash
    source ~/turtlebot3_ws/install/setup.bash
    ```

3. Set the robot model environment variable:

    ```bash
    export TURTLEBOT3_MODEL=burger_cam
    ```

4. Launch the teleop node:

    ```bash
    ros2 run turtlebot3_teleop teleop_keyboard
    ```

### Keyboard Controls

| Key | Action |
|-----|--------|
| `W` | Move Forward |
| `X` | Move Backward |
| `A` | Turn Left |
| `D` | Turn Right |
| `S` | Stop (full stop) |

> ⚠️ Make sure your **terminal window is selected/active** when pressing keys — otherwise the keypresses won't register in the teleop node.

---

