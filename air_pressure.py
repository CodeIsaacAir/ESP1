import machine
import time

# Define your sensor's connections
sck_pin = 12  # GPIO pin for the clock signal
out_pin = 14  # GPIO pin for the data output
vcc_pin = 5   # GPIO pin for sensor power supply (if applicable)

# Initialize GPIO pins
sck = machine.Pin(sck_pin, machine.Pin.OUT)
out = machine.Pin(out_pin, machine.Pin.IN)

# Power up the sensor (if required)
if vcc_pin:
    vcc = machine.Pin(vcc_pin, machine.Pin.OUT)
    vcc.on()

# Function to read data from the sensor
def read_sensor():
    # Read raw data from the sensor
    raw_data = 0
    for i in range(24):
        sck.on()
        time.sleep_us(5)
        raw_data = (raw_data << 1) | out.value()
        sck.off()
        time.sleep_us(1)

    # Convert raw data to pressure reading (you'll need to adjust this)
    pressure_kpa = raw_data 

    return pressure_kpa

# Read data from the sensor and print it
while True:
    pressure = read_sensor()
    print("Pressure (kPa):", pressure)
    time.sleep(1)  # Adjust the interval as needed
