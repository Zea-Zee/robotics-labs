ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py

ros2 run turtlesim turtle_teleop_key

ros2 run tf2_tools view_frames

ros2 run tf2_ros tf2_echo turtle2 turtle1 > transform.txt
