import Jetson.GPIO as GPIO
import time

#GPIO
GPIO.setmode(GPIO.BOARD)
servo_pin = 33 #pin number
GPIO.setup(servo_pin, GPIO.OUT)

# 初始化 PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency
pwm.start(0)

try:
    while True:
        # 90°
        pwm.ChangeDutyCycle(7.5)  # 7.5% 
        time.sleep(1)
        # 0°
        pwm.ChangeDutyCycle(2.5)  # 2.5%
        time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()