ros2 launch robot_bringup diff_drive.launch.py


os2 run rqt_robot_steering rqt_robot_steering --ros-args -r /cmd_vel:="/robot/cmd_vel"
/
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:="/robot/cmd_vel"


ros2 topic list
ros2 topic info /robot/cmd_vel
ros2 topic echo /robot/cmd_vel
