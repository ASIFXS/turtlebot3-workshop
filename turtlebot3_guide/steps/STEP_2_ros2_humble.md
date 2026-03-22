# STEP 2 — Install ROS 2 Humble

> ⚠️ **Got an error in this step?** → See [ERR_2_ros2_install.md](../errors/ERR_2_ros2_install.md)

> 📝 **Note (Galactic → Humble):** The Medium series uses Galactic on Ubuntu 20.04.
> We use **Humble on Ubuntu 22.04** — same structure, different distro names.

---

## 2.1 — Set Locale

```bash
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Verify
locale
```

---

## 2.2 — Add ROS 2 Repository

```bash
sudo apt install software-properties-common curl -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
  http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
```

---

## 2.3 — Install ROS 2 Humble Desktop

```bash
sudo apt install ros-humble-desktop -y
```

This installs ROS core + RViz2 + demo packages. Takes a few minutes.

---

## 2.4 — Source ROS 2 (Temporary Test)

```bash
source /opt/ros/humble/setup.bash

# Verify
lsb_release -a

echo $ROS_DISTRO
# Expected: ros2 cli version X.X.X
```

---

## 2.5 — Add to ~/.bashrc (Permanent)

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## ✅ Checklist Before Moving On

- [ ] `ros2 --version` works
- [ ] `ros2 topic list` runs without error
- [ ] `source /opt/ros/humble/setup.bash` is in your `~/.bashrc`

➡️ **Next:** [STEP_3_workspace_vcstool.md](STEP_3_workspace_vcstool.md)
