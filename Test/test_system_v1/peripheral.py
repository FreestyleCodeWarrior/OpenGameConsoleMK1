# Objects of Peripherals are created in this class 
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Peripheral:
    def __init__(self, HardwareID, LedMatrix, LedDigitalTube, Buzzer, Buttons, SPI, SoftI2C, Pin, Timer):
        hardwareID = HardwareID()
        self._init_screen(hardwareID, LedMatrix, SPI, Pin)
        self._init_timer(hardwareID, LedDigitalTube, SoftI2C, Pin)
        self._init_scorer(hardwareID, LedDigitalTube, SoftI2C, Pin)
        self._init_buttons(hardwareID, Buttons, Timer, Pin)
        self._init_buzzer(hardwareID, Buzzer, Timer, Pin)
    
    def _init_screen(self, hardwareID, LedMatrix, SPI, Pin):
        spi = SPI(hardwareID.screen_spi_id)
        cs_0 = Pin(hardwareID.screen_cs_0)
        cs_1 = Pin(hardwareID.screen_cs_1)
        self.screen = LedMatrix(spi, [cs_0, cs_1])
    
    def _init_timer(self, hardwareID, LedDigitalTube, SoftI2C, Pin):
        scl = Pin(hardwareID.timer_scl)
        sda = Pin(hardwareID.timer_sda)
        self.timer = LedDigitalTube(SoftI2C, scl, sda)
    
    def _init_scorer(self, hardwareID, LedDigitalTube, SoftI2C, Pin):
        scl = Pin(hardwareID.scorer_scl)
        sda = Pin(hardwareID.scorer_sda)
        self.scorer = LedDigitalTube(SoftI2C, scl, sda)
    
    def _init_buttons(self, hardwareID, Buttons, Timer, Pin):
        up_pin = Pin(hardwareID.button_up_pin)
        down_pin = Pin(hardwareID.button_down_pin)
        left_pin = Pin(hardwareID.button_left_pin)
        right_pin = Pin(hardwareID.button_right_pin)
        ok_pin = Pin(hardwareID.button_ok_pin)
        back_pin = Pin(hardwareID.button_back_pin)
        timer = Timer(hardwareID.button_timer_id)
        self.buttons = Buttons(timer, up=up_pin, down=down_pin, right=right_pin, left=left_pin, ok=ok_pin,back=back_pin)
    
    def _init_buzzer(self, hardwareID, Buzzer, Timer, Pin):
        pin = Pin(hardwareID.buzzer_pin)
        timer = Timer(hardwareID.buzzer_timer_id)
        self.buzzer = Buzzer(pin, timer)
        