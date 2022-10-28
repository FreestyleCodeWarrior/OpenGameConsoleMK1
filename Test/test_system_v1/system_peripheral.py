from machine import Pin
from machine import SPI
from machine import SoftI2C
from machine import Timer

from driver_max7219 import LedMatrix
from driver_tm1650 import LedDigitalTube
from driver_buttons import Buttons
from driver_buzzer import Buzzer


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


class Peripheral(HardwareID):
    def __init__(self):
        super().__init__()
        self._init_screen(LedMatrix, SPI, Pin)
        self._init_timer(LedDigitalTube, SoftI2C, Pin)
        self._init_scorer(LedDigitalTube, SoftI2C, Pin)
        self._init_buttons(Buttons, Timer, Pin)
        self._init_buzzer(Buzzer, Timer, Pin)


    def _init_screen(self, LedMatrix, SPI, Pin):
        spi = SPI(self.screen_spi_id)
        cs_0 = Pin(self.screen_cs_0)
        cs_1 = Pin(self.screen_cs_1)
        self.screen = LedMatrix(spi, [cs_0, cs_1])


    def _init_timer(self, LedDigitalTube, SoftI2C, Pin):
        scl = Pin(self.timer_scl)
        sda = Pin(self.timer_sda)
        self.timer = LedDigitalTube(SoftI2C, scl, sda)


    def _init_scorer(self, LedDigitalTube, SoftI2C, Pin):
        scl = Pin(self.scorer_scl)
        sda = Pin(self.scorer_sda)
        self.scorer = LedDigitalTube(SoftI2C, scl, sda)


    def _init_buttons(self, Buttons, Timer, Pin):
        up_pin = Pin(self.button_up_pin)
        down_pin = Pin(self.button_down_pin)
        left_pin = Pin(self.button_left_pin)
        right_pin = Pin(self.button_right_pin)
        ok_pin = Pin(self.button_ok_pin)
        back_pin = Pin(self.button_back_pin)
        timer = Timer(self.button_timer_id)
        self.buttons = Buttons(timer,
            up=up_pin,
            down=down_pin,
            right=right_pin,
            left=left_pin,
            ok=ok_pin,
            back=back_pin)


    def _init_buzzer(self, Buzzer, Timer, Pin):
        pin = Pin(self.buzzer_pin)
        timer = Timer(self.buzzer_timer_id)
        self.buzzer = Buzzer(pin, timer)
