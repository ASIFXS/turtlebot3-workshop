cmake_minimum_required(VERSION 3.8)
project(workshop_task1)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

# Install Python package (the folder with __init__.py)
ament_python_install_package(${PROJECT_NAME})

# Install Python scripts so ros2 run can find them
install(PROGRAMS
  workshop_task1/move_robot.py
  workshop_task1/drawcircle.py 
  workshop_task1/navigate_to_goal_ANSWER.py

  DESTINATION lib/${PROJECT_NAME}
)
#install(
#  DIRECTORY launch
#  DESTINATION share/${PROJECT_NAME}
#)
ament_package()