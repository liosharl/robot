import time
import requests

# Function to get the robot's current location (replace with your actual code)
def get_robot_location():
    # Implement your code to retrieve the robot's location here
    # Return the location as a tuple (latitude, longitude) or in any suitable format
    # Example: return (42.12345, -71.98765)
    pass

# Replace with the URL where you want to send the location data
report_url = 'https://example.com/report_location'

while True:
    try:
        # Get the robot's current location
        location = get_robot_location()
        
        # Timestamp the location
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Log the location
        print(f"Location at {timestamp}: {location}")
        
        # Send the location to a remote server (replace with your reporting code)
        response = requests.post(report_url, json={'timestamp': timestamp, 'location': location})
        
        if response.status_code == 200:
            print("Location reported successfully")
        else:
            print("Failed to report location")
        
        # Wait for 5 minutes (300 seconds) before the next update
        time.sleep(300)
        
    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl+C)
        print("Program terminated by user")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
