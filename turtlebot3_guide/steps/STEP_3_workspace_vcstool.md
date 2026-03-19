# STEP 3 — Create Workspace & Clone Repos with vcstool

> ⚠️ **Got an error in this step?** → See [ERR_3_workspace_vcstool.md](../errors/ERR_3_workspace_vcstool.md)

> 📝 **What is vcstool?**
> `vcstool` clones multiple git repositories at once using a single `.repos` YAML file.
> It is the recommended way to set up TurtleBot3 from source instead of apt packages.
> This gives you more control and avoids version mismatch issues.

---

## 3.1 — Create the Workspace

```bash
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws
```

---

## 3.2 — Create the .repos File

Create `turtlebot3_humble.repos` inside `~/turtlebot3_ws/`:

```bash
gedit ~/turtlebot3_ws/turtlebot3_humble.repos
```

Paste exactly this content:

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

Save and close the file.

---

## 3.3 — Clone All Repos with vcstool

```bash
cd ~/turtlebot3_ws
vcs import src < turtlebot3_humble.repos
```

Expected output — you should see all 5 repos being cloned:
```
Cloning into 'turtlebot3/turtlebot3'...
Cloning into 'turtlebot3/turtlebot3_msgs'...
Cloning into 'turtlebot3/turtlebot3_simulations'...
Cloning into 'utils/DynamixelSDK'...
Cloning into 'utils/hls_lfcd_lds_driver'...
```

Verify the structure:
```bash
ls ~/turtlebot3_ws/src/
# Should show: turtlebot3/  utils/

ls ~/turtlebot3_ws/src/turtlebot3/
# Should show: turtlebot3  turtlebot3_msgs  turtlebot3_simulations
```

---

## 3.4 — Initialize rosdep (First Time Only)

```bash
sudo rosdep init
rosdep update
```

If `sudo rosdep init` says "file already exists", that is fine — skip it and just run `rosdep update`.

---

## ✅ Checklist Before Moving On

- [ ] `~/turtlebot3_ws/src/turtlebot3/turtlebot3` exists
- [ ] `~/turtlebot3_ws/src/turtlebot3/turtlebot3_simulations` exists
- [ ] `~/turtlebot3_ws/src/utils/DynamixelSDK` exists
- [ ] `rosdep update` ran without errors

➡️ **Next:** [STEP_4_gazebo_build.md](STEP_4_gazebo_build.md)
