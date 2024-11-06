from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='Leonardo'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='Raphael'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim3',
            executable='turtlesim_node',
            name='Donatello'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim4',
            executable='turtlesim_node',
            name='Michelangelo'
        ),
    ])
