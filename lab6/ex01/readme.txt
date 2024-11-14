ros2 launch robot_bringup robot_lidar.launch.py


ros2 run rqt_robot_steering rqt_robot_steering --ros-args -r /cmd_vel:="/robot/cmd_vel"


ros2 topic list
ros2 topic info /robot/scan
ros2 topic echo /robot/scan
