ros2 run turtlesim turtlesim_node


ros2 run turtlesim turtle_teleop_key


ros2 bag record /turtle1/cmd_vel -o turtle_cmd_vel.mcap


ros2 topic echo /turtle1/pose > pose_speed_x1.yaml
ros2 bag play turtle_cmd_vel.mcap

ros2 topic echo /turtle1/pose > pose_speed_x2.yaml
ros2 bag play turtle_cmd_vel.mcap --rate 2
