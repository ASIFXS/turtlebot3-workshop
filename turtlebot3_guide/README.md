# 🤖 TurtleBot3 Simulation — ROS 2 Humble Complete Guide
> **OS:** Ubuntu 22.04 | **ROS:** Humble Hawksbill | **Gazebo:** Classic 11  
> Built from source using `vcstool` + `.repos` file

---

## 📁 Guide Structure

```
turtlebot3_guide/
├── README.md                          ← Start here
├── steps/
│   ├── STEP_1_clean_and_prereqs.md
│   ├── STEP_2_ros2_humble.md
│   ├── STEP_3_workspace_vcstool.md
│   ├── STEP_4_gazebo_build.md
│   ├── STEP_5_env_variables.md
│   ├── STEP_6_run_simulation.md
│   ├── STEP_7_slam_mapping.md
│   └── STEP_8_navigation_nav2.md
└── errors/
    ├── ERR_1_clean_prereqs.md
    ├── ERR_2_ros2_install.md
    ├── ERR_3_workspace_vcstool.md
    ├── ERR_4_gazebo_build.md
    ├── ERR_5_env_variables.md
    ├── ERR_6_simulation.md
    ├── ERR_7_slam.md
    └── ERR_8_navigation.md
```

---

## 🔢 Step Order

| Step | File | What it does |
|------|------|-------------|
| 1 | [STEP_1](steps/STEP_1_clean_and_prereqs.md) | Clean old Gazebo, install tools |
| 2 | [STEP_2](steps/STEP_2_ros2_humble.md) | Install ROS 2 Humble |
| 3 | [STEP_3](steps/STEP_3_workspace_vcstool.md) | Workspace + clone with vcstool |
| 4 | [STEP_4](steps/STEP_4_gazebo_build.md) | Gazebo + colcon build |
| 5 | [STEP_5](steps/STEP_5_env_variables.md) | Environment variables |
| 6 | [STEP_6](steps/STEP_6_run_simulation.md) | Run simulation + teleop |
| 7 | [STEP_7](steps/STEP_7_slam_mapping.md) | SLAM mapping |
| 8 | [STEP_8](steps/STEP_8_navigation_nav2.md) | Nav2 autonomous navigation |

> 💡 Got an error? Each step file links to its matching `errors/ERR_X_...md` at the top.

---

## 📄 The `.repos` File (turtlebot3_humble.repos)

```yaml
repositories:
  turtlebot3/turtlebot3:
    type: git
    url: https://github.com/ROBOTIS-GIT/turtlebot3.git
    version: humble
  turtlebot3/turtlebot3_msgs:
    type: git
    url: https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
    version: humble
  turtlebot3/turtlebot3_simulations:
    type: git
    url: https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
    version: humble
  utils/DynamixelSDK:
    type: git
    url: https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    version: humble
  utils/hls_lfcd_lds_driver:
    type: git
    url: https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
    version: humble
```

---
*Based on [ROS 2 TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/) — updated → Humble*
