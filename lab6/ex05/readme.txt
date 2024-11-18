colcon build --packages-select robot_app robot_bringup robot_description robot_depth
source install/setup.bash

ros2 launch robot_depth robot_depth.launch.py


python3 ~/Desktop/robotics-labs/lab6/ex05/depth_stream.py
