# ROS 2 Humble Setup Guide — Ubuntu 22.04

Copy and paste each block directly into your terminal.

---

## 1. System Prep & Locale Setup

Fix any broken packages and set the correct locale (required for ROS 2):

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install -y
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

---

## 2. Add the ROS 2 Humble Repository

Downloads the ROS 2 security keys and adds the repository to your system sources:

```bash
sudo apt install software-properties-common curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

---

## 3. Install All Dependencies

Installs ROS 2, Gazebo, build tools (colcon, cmake, C++ essentials), vcstool, rosdep, and SLAM/Nav2 packages:

```bash
sudo apt update
sudo apt install -y \
  ros-humble-desktop \
  gazebo11 \
  ros-humble-gazebo-ros-pkgs \
  ros-humble-gazebo-ros2-control \
  ros-humble-cartographer-ros \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  python3-colcon-common-extensions \
  python3-rosdep \
  python3-vcstool \
  python3-pip \
  git \
  build-essential \
  cmake \
  wget
```

---

## 4. Initialize rosdep

Used to resolve ROS dependencies.

> **Note:** If you get a *"default sources list already exists"* error on the first command, ignore it and run only the second command.

```bash
sudo rosdep init
rosdep update --include-eol-distros
```

---

## 5. Setup the Terminal Environment

Automatically sources ROS 2 on every new terminal and sets the default TurtleBot3 model:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "export TURTLEBOT3_MODEL=burger_cam" >> ~/.bashrc
source ~/.bashrc
```

---

✅ Once all 5 steps are complete, your laptop is ready for the workshop!

Next steps: create your workspace, use `vcs import`, and build with `colcon`.
