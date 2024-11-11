colcon build --packages-select full_name_pkg
colcon build --packages-select full_name

source install/setup.bash

ros2 run full_name service


ros2 run full_name client Ivanov Ivan Ivanovich
