ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'move_forward'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'turn_right'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'move_forward'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'turn_left'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'turn_left'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'turn_left'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'move_forward'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'turn_left'"
ros2 topic pub -1 cmd_text std_msgs/msg/String "data: 'move_backward'"


ros2 run text_to_cmd_vel text_to_cmd_vel


ros2 run turtlesim  turtlesim_node
