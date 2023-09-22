import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Global variables for camera angles
pan_angle = 0.0  # Initialize pan angle
tilt_angle = 0.0  # Initialize tilt angle

# Define a callback function to handle camera control commands
def camera_control_callback(data):
    global pan_angle, tilt_angle
    command = data.data.lower()
    
    if "pan_left" in command:
        pan_angle += 0.1  # Adjust the angle increment as needed
    elif "pan_right" in command:
        pan_angle -= 0.1
    elif "tilt_up" in command:
        tilt_angle += 0.1
    elif "tilt_down" in command:
        tilt_angle -= 0.1

    # Implement logic to control the camera's pan-tilt mechanism using pan_angle and tilt_angle
    # You will need to use the appropriate libraries or APIs for your camera hardware

# Initialize the ROS node
if __name__ == '__main__':
    rospy.init_node('camera_controller', anonymous=True)
    rospy.Subscriber('camera_command', String, camera_control_callback)
    
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Implement camera control logic here, using pan_angle and tilt_angle
        # Publish camera angles to control the camera's movement
        
        # Example: Publish angles to control the camera (adjust as needed)
        camera_command = Twist()
        camera_command.angular.x = pan_angle
        camera_command.angular.y = tilt_angle
        # Publish the camera_command
        
        rate.sleep()
