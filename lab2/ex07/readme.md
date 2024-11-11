ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: 'Leonardo'}"
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 0, theta: 0.2, name: 'Raphael'}"
ros2 service call /spawn turtlesim/srv/Spawn "{x: 0, y: 2, theta: 0.2, name: 'Donatello'}"
ros2 service call /spawn turtlesim/srv/Spawn "{x: 0, y: 0, theta: 0.2, name: 'Michelangelo'}"
ros2 param set /turtlesim background_g 124
