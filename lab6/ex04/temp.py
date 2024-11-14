def move(self):
    """Moves the turtle to the goal."""
    vel_msg = Twist()
    laser = self.scan.ranges
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    if (len(laser)!=0):
        threshold_distance = 0.4
        close_points = sum([1 for dist in laser[170:190] if dist < threshold_distance])
        if close_points < 15:
            vel_msg.linear.x = 1.0
    self.velocity_publisher.publish(vel_msg)
