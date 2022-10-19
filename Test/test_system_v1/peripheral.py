# Objects of Peripherals are created in this class 
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Peripheral:
    def __init__(self, constant, LedMatrix, LedDigitalTube, Buzzer, Buttons, SPI, SoftI2C, Pin, Timer):
        self._init_screen(constant, LedMatrix, SPI, Pin)
        self._init_timer(constant, LedDigitalTube, SoftI2C, Pin)
        self._init_scorer(constant, LedDigitalTube, SoftI2C, Pin)
        self._init_buttons(constant, Buttons, Timer, Pin)
        self._init_buzzer(constant, Buzzer, Timer, Pin)
    
    def _init_screen(self, constant, LedMatrix, SPI, Pin):
        spi = SPI(constant.screen_spi_id)
        cs_0 = Pin(constant.screen_cs_0)
        cs_1 = Pin(constant.screen_cs_1)
        self.screen = LedMatrix(spi, [cs_0, cs_1])
    
    def _init_timer(self, constant, LedDigitalTube, SoftI2C, Pin):
        scl = Pin(constant.timer_scl)
        sda = Pin(constant.timer_sda)
        self.timer = LedDigitalTube(SoftI2C, scl, sda)
    
    def _init_scorer(self, constant, LedDigitalTube, SoftI2C, Pin):
        scl = Pin(constant.scorer_scl)
        sda = Pin(constant.scorer_sda)
        self.scorer = LedDigitalTube(SoftI2C, scl, sda)
    
    def _init_buttons(self, constant, Buttons, Timer, Pin):
        up_pin = Pin(constant.button_up_pin)
        down_pin = Pin(constant.button_down_pin)
        left_pin = Pin(constant.button_left_pin)
        right_pin = Pin(constant.button_right_pin)
        ok_pin = Pin(constant.button_ok_pin)
        back_pin = Pin(constant.button_back_pin)
        timer = Timer(constant.button_timer_id)
        self.buttons = Buttons(timer, up=up_pin, down=down_pin, right=right_pin, left=left_pin, ok=ok_pin,back=back_pin)
    
    def _init_buzzer(self, constant, Buzzer, Timer, Pin):
        pin = Pin(constant.buzzer_pin)
        timer = Timer(constant.buzzer_timer_id)
        self.buzzer = Buzzer(pin, timer)
        