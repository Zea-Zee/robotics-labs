import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


from launch_ros.actions import Node


def generate_launch_description():
    # radius_arg = DeclareLaunchArgument(
    #     'radius', default_value='1.0', description='Расстояние от черепахи до морковки'
    # )
    # direction_arg = DeclareLaunchArgument(
    #     'direction_of_rotation', default_value='1', description='1 - по часовой стрелке, -1 - против часовой'
    # )

    demo_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('learning_tf2_py'), 'launch'),
            '/turtle_tf2_demo.launch.py']),
       launch_arguments={'target_frame': 'carrot1'}.items(),
       )

    return LaunchDescription([
        demo_nodes,
        Node(
            package='learning_tf2_py',
            executable='dynamic_frame_tf2_broadcaster',
            name='dynamic_broadcaster',
            # parameters=[
            #     {'radius': LaunchConfiguration('radius')},
            #     {'direction_of_rotation': LaunchConfiguration('direction_of_rotation')}
            # ]
        ),
    ])
