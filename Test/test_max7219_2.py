# Test for hardware driver of LED matrix with max7219
# MicroPython v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

from micropython import const

# declare of constant register addresses
NOOP = const(0x0)
DIGIT0 = const(0x1)
DIGIT1 = const(0x2)
DIGIT2 = const(0x3)
DIGIT3 = const(0x4)
DIGIT4 = const(0x5)
DIGIT5 = const(0x6)
DIGIT6 = const(0x7)
DIGIT7 = const(0x8)
DECODEMODE = const(0x9)
INTENSITY = const(0xA)
SCANLIMIT = const(0xB)
SHUTDOWN = const(0xC)
DISPLAYTEST = const(0xF)

class Max7219LEDMatrix:
    def __init__(self, spi, cs, num):
        # spi (an instance of machine.SPI): serial phripheral interface
        # cs (an instance of machine.Pin): chip select pin
        # num (an integer greater than 0): number of daisy-chained 8*8 LED matrix
        # slice_range (tuple): used for slice a line of data into several list with 8 elements
        self.spi = spi
        self.cs = cs
        self.num = num
        self.slice_range = tuple((i*8, i*8+8) for i in range(num))
        self._init()
    
    def _init(self):
        # initialize SPI, CS and registers.
        self.spi.init(baudrate=800000, polarity=0, phase=0, firstbit=spi.MSB)
        self.cs.init(mode=Pin.OUT, drive=Pin.DRIVE_0)
        for a, d in ((SHUTDOWN, 0x0),
                     (DISPLAYTEST, 0x0),
                     (SCANLIMIT, 0x7),
                     (DECODEMODE, 0x0),
                     (INTENSITY, 0x6))
            self.write_all(a, d)
        # make sure every LED is initially turned off
        for i in range(8):
            self.write_all(DIGIT0+i, 0b00000000)
    
    def write_all(self, addr, data):
        # write same addr+data into all max7219 
        self.cs.off()
        for _ in range(self.num):
            self.spi.write(bytearray([addr, data]))
        self.cs.on()
    
    def write_image(self, lines):
        for x in range(8):
            self.cs.off()
            for y in range(self.num):
                self.spi.write(bytearray(DIGIT0+x,\
                eval("0b{}{}{}{}{}{}{}{}".format(*lines[x][8*y:8*y+8]))))
            self.cs.on()
    
    def test(self):
        self.write_all(DISPLAYTEST, 0x1)
        
    def fill(self):
        for i in range(8):
            self.write_all(DIGIT0+i, 0b11111111)
    
    def empty(self):
        for i in range(8):
            self.write_all(DIGIT0+i, 0b11111111)
    
    def on(self):
        self.write_all(SHUTDOWN, 0)
    
    def off(self):
        self.write_all(SHUTDOWN, 1)
        
    
    
                
            
            
            


