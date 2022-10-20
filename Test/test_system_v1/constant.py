# Constants called by other command statement
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class HardwareID:
    def __init__(self):
        self._screen()
        self._timer()
        self._scorer()
        self._button()
        self._buzzer()
    
    def _screen(self):
        self.screen_spi_id = 1
        self.screen_cs_0 = 32
        self.screen_cs_1 = 33
    
    def _timer(self):
        self.timer_scl = 18
        self.timer_sda = 19
    
    def _scorer(self):
        self.scorer_scl = 25
        self.scorer_sda = 26
    
    def _button(self):
        self.button_up_pin = 2
        self.button_down_pin = 4
        self.button_left_pin = 5
        self.button_right_pin = 22
        self.button_ok_pin = 23
        self.button_back_pin = 27
        self.button_timer_id = 0
    
    def _buzzer(self):
        self.buzzer_pin = 0
        self.buzzer_timer_id = 1
        

class Icon:
    def __init__(self):
        self.sun = (
            0b10011001,
            0b01011010,
            0b00000000,
            0b11011011,
            0b11011011,
            0b00000000,
            0b01011010,
            0b10011001)
        self.speaker = (
            0b00000100,
            0b00010110,
            0b00110110,
            0b11110110,
            0b11110110,
            0b00110110,
            0b00010110,
            0b00000100)
        self.circle = (
            0b00011000,
            0b00111100,
            0b01100110,
            0b11000011,
            0b11000011,
            0b01100110,
            0b00111100,
            0b00011000)
        self.cross = (
            0b11000011,
            0b11100111,
            0b01111110,
            0b00111100,
            0b00111100,
            0b01111110,
            0b11100111,
            0b11000011)
        self.tool = (
             0b01010010,
             0b01010010,
             0b01010010,
             0b01011110,
             0b01001100,
             0b11101100,
             0b11101100,
             0b11101100)
        self.monster = (
             0b00100100,
             0b00100100,
             0b01111110,
             0b11011011,
             0b11111111,
             0b11111111,
             0b10100101,
             0b00100100)
        
        self.up_ind = ((3, 9), (4, 9), (3, 10), (4, 10))
        self.down_ind = ((3, 13), (4, 13), (3, 14), (4, 14))
        self.left_ind = ((1, 11), (2, 11), (1, 12), (2, 12))
        self.right_ind = ((5, 11), (6, 11), (5, 12), (6, 12))

class FileName:
    def __init__(self):
        self.conf = "configuration.json"
        self.score_records = "scores.json"











