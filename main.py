#main file
import threading
from sensor_read import read_sensor_data 
from motor_control import motor_control_loop
from gui import ExoGUI

def sensor_update_call(sensor_active, torque, gait_phase):
    #connect gui, motor, and sensor
    gui.update(sensor_active, torque, gait_phase)

if __name__ == "__main__":
    gui = ExoGUI

    #enable sensor
    sensor_thread = threading.Thread(target=read_sensor_data, args=(sensor_update_call,), daemon=True)
    sensor_thread.start()

    #enable motor
    motor_thread = threading.Thread(target=motor_control_loop, daemon=True)
    motor_thread.start()

    #enable gui
    gui.run()