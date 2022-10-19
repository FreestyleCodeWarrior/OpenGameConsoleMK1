# Constant class consisting with constants called by other objects
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Constant:
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
        
        