import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Define a callback function to handle the "pick" command
def pick_callback(data):
    if data.data.lower() == "pick":
        # Implement logic to control the robot's arm or gripper to pick an object
        # You will need to use the appropriate libraries or APIs for your specific hardware

# Define a function to control the robot's movement
def move_robot():
    rospy.init_node('robot_controller', anonymous=True)
    rospy.Subscriber('pick_command', String, pick_callback)
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
