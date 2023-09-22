import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(data):
    # Define obstacle detection logic based on laser scan data
    # If obstacles are detected, calculate and execute an avoidance strategy
    if any(distance < 0.5 for distance in data.ranges):
        # Implement avoidance logic here
        # Adjust robot's movement commands to avoid obstacles

def move_robot():
    rospy.init_node('robot_controller', anonymous=True)
    rospy.Subscriber('scan', LaserScan, callback)
    cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Move the robot forward at a constant speed
        cmd_vel = Twist()
        cmd_vel.linear.x = 0.2  # Adjust the speed as needed
        cmd_vel.angular.z = 0.0
        cmd_vel_pub.publish(cmd_vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
