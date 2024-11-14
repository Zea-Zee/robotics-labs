ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo.launch.py

ros2 run tf2_tools view_frames

ros2 launch learning_tf2_py turtle_tf2_fixed_frame_demo.launch.py target_frame:=carrot1


colcon build --packages-select learning_tf2_py
ros2 launch ex02 turtlesim_with_carrot.launch.py radius:=1.0 direction_of_rotation:=1

