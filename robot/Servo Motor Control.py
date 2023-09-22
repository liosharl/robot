import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up a GPIO pin as PWM output
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz PWM frequency

# Move the servo to a specific angle
def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Example usage:
try:
    set_servo_angle(90)  # Move servo to 90 degrees
    time.sleep(2)
    set_servo_angle(0)   # Move servo to 0 degrees
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
