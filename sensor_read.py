#sensor read 
import time
import random

try: 
    import board
    import busio
    import adafruit_mpr121
    hardware_available = True
except ImportError:
    hardware_available = False

if hardware_available:
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)

def get_sensor_value (channel = 0):
    if hardware_available:
        return mpr121[channel].value
    else: 
        return random.choice([True, False])

def read_sensor_data(update_callback, interval = 0.1):
    while True:
        sensor_active = get_sensor_value(0)

        if sensor_active:
            #我不知道具体的值是多少
            torque = 10
            gait_phase = "Stance"
        else: 
            torque = 5
            gait_phase = "Swing"
        update_callback(sensor_active,torque, gait_phase)
        time.sleep(interval)