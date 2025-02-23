import sensor_read
import unittest 
from unittest.mock import patch, MagicMock
# test_sensor.py
class TestSensor(unittest.TestCase):
    @patch('sensor_read.adafruit_mpr121')
    @patch('sensor_read.busio')
    @patch('sensor_read.board')
    def test_get_sensor_value(self, mock_board, mock_busio, mock_adafruit):
        
        fake_touch_sensor = MagicMock()
        fake_touch_sensor.value = True

        
        fake_mpr121_instance = MagicMock()
        fake_mpr121_instance.__getitem__.return_value = fake_touch_sensor

        
        mock_adafruit.MPR121.return_value = fake_mpr121_instance

        result = sensor_read.get_sensor_value(0)

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

