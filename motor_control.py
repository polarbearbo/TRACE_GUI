import time

#try whether GPIO is able or not
try: 
    import Jetson.GPIO as GPIO
    hardware_available = True 
except ImportError:
    hardware_available = False

#check whether hardware is available
if hardware_available:
    GPIO.setmode(GPIO.BOARD)
    servo_pin = 0 # depends on the pin number
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, 50) 
    pwm.start(0)
else:  
    class Dummy:
        def ChangeDutyCycle(self, duty):
            print(f"Simulated PWM duty: {duty}")
        def stop (self): 
            pass
    pwm = Dummy()

def motor_control_loop(interval = 1):
    try:
        while True:
            pwm.ChangeDutyCycle(7.5)
            time.sleep(interval)
            pwm.ChangeDutyCycle(2.5)
            time.sleep(interval)
    except KeyboardInterrupt:
       if hardware_available:
           pwm.stop()
           GPIO.cleanup() 