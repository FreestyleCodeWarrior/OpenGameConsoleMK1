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
        pass
    
    
    def diode(self):
        return (0b01111110,
                0b01000010,
                0b01011010,
                0b01011010,
                0b11111111,
                0b00100100,
                0b00100100,
                0b00000100)
    
    
    def speaker(self):
        return (0b00000100,
                0b00010110,
                0b00110110,
                0b11110110,
                0b11110110,
                0b00110110,
                0b00010110,
                0b00000100)
    
    
    def circle(self):
        return (0b00011000,
                0b00111100,
                0b01100110,
                0b11000011,
                0b11000011,
                0b01100110,
                0b00111100,
                0b00011000)
    
    
    def cross(self):
        return (0b11000011,
                0b11100111,
                0b01111110,
                0b00111100,
                0b00111100,
                0b01111110,
                0b11100111,
                0b11000011)
    
    
    def tool(self):
        return (0b01001001,
                0b01001001,
                0b01001001,
                0b01001111,
                0b11100110,
                0b11100110,
                0b11100110,
                0b11100110)


    def disk(self):
        return (0b00011111,
                0b00100001,
                0b01000001,
                0b10000001,
                0b10111101,
                0b10100101,
                0b10100101,
                0b11111111)


    def monster(self):
        return (0b00100100,
                0b00100100,
                0b01111110,
                0b11011011,
                0b11111111,
                0b11111111,
                0b10100101,
                0b00100100)
    
    
    def fill(self):
        return tuple(0b11111111 for _ in range(8))
    
    
    def empty(self):
        return tuple(0b00000000 for _ in range(8))
    
    
    def indicator(self, up=False, down=False, left=False, right=False):
        rows = [0]
        
        if up:
            rows += [24, 24]
        else:
            rows += [0, 0]
            
        if left and right:
            rows += [102, 102]
        elif left:
            rows += [96, 96]
        elif right:
            rows += [6, 6]
        else:
            rows += [0, 0]
            
        if down:
            rows += [24, 24]
        else:
            rows += [0, 0]
            
        rows.append(0)
        
        return tuple(rows)