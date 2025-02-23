# test_motor.py
import unittest
from unittest.mock import patch, MagicMock
import motor_control

class TestMotor(unittest.TestCase):
    @patch('motor_control.GPIO')
    def test_motor_control_loop(self, mock_Jetson):
        # 创建一个模拟的 PWM 对象
        fake_pwm = MagicMock()
        # 当调用 PWM() 时返回 fake_pwm
        mock_Jetson.PWM.return_value = fake_pwm

        import threading, time
        loop_thread = threading.Thread(target=motor_control.motor_control_loop, kwargs={'interval':0.1}, daemon=True)
        loop_thread.start()
        time.sleep(0.5)  # 运行0.5秒

        self.assertTrue(fake_pwm.ChangeDutyCycle.called)
        # 结束测试（实际测试中可能需要更优雅的方式终止循环）

if __name__ == '__main__':
    unittest.main()
