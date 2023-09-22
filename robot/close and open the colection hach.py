import RPi.GPIO as GPIO
import time

# Set up GPIO pins for the servo motor (Raspberry Pi GPIO example)
servo_pin = 18  # Adjust the GPIO pin as needed
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Function to open the collection box
def open_collection_box():
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz PWM frequency
    pwm.start(0)
    duty_cycle = 7.5  # Adjust the duty cycle for your servo
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    pwm.stop()

# Function to close the collection box
def close_collection_box():
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz PWM frequency
    pwm.start(0)
    duty_cycle = 2.5  # Adjust the duty cycle for your servo
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    pwm.stop()

# Example usage:
try:
    open_collection_box()  # Open the collection box
    time.sleep(5)  # Wait for 5 seconds (or perform collection)
    close_collection_box()  # Close the collection box
except KeyboardInterrupt:
    pass

# Cleanup GPIO pins
GPIO.cleanup()
