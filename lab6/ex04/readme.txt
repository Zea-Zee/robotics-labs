colcon build --packages-select robot_app robot_bringup robot_description robot_lidar
source install/setup.bash


ros2 launch robot_lidar robot_lidar.launch.py
