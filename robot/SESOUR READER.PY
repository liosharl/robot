import Adafruit_DHT

# Sensor type and GPIO pin
sensor = Adafruit_DHT.DHT22
pin = 4

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
        else:
            print('Failed to retrieve data')
        time.sleep(2)
except KeyboardInterrupt:
    pass
