# Construct and Test hardware driver of LED matrix with max7219
# MicroPython v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

from micropython import const

# declare register addresses as constants
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
        # spi (machine.SPI): serial phripheral interface
        # cs (machine.Pin): chip select pin
        # num (integer greater than 0): number of daisy-chained 8*8 LED matrix
        # slice (tuple): for split a line of data into several list with 8 elements
        self.spi = spi
        self.cs = cs
        self.num = num
        self.slice = tuple((i*8, i*8+8) for i in range(num))
        self._init()
    
    def _init(self):
        # initialize SPI, CS and registers.
        self.spi.init(baudrate=900000, polarity=0, phase=0, firstbit=self.spi.MSB)
        self.cs.init(mode=Pin.OUT, drive=Pin.DRIVE_0)
        for a, d in ((SHUTDOWN, 0x1),
                     (DISPLAYTEST, 0x0),
                     (SCANLIMIT, 0x7),
                     (DECODEMODE, 0x0),
                     (INTENSITY, 0x6)):
            self.write_all(a, d)
        # make sure every LED is turned off
        self.empty()
    
    def write_all(self, addr, data):
        # write same addr+data into register of every max7219 
        self.cs.off()
        for _ in range(self.num):
            self.spi.write(bytearray([addr, data]))
        self.cs.on()
    
    def write_image(self, lines):
        # write image line by line and then show 
        for x in range(8):
            self.cs.off()
            for y in range(self.num):
                self.spi.write(bytearray([DIGIT0+x,\
                eval("0b{}{}{}{}{}{}{}{}".format(*lines[x][self.slice[y][0]:self.slice[y][1]]))]))
            self.cs.on()
    
    def test(self, on):
        # turn on/off display test mode
        if on:
            self.write_all(DISPLAYTEST, 0x1)
        else:
            self.write_all(DISPLAYTEST, 0x0)
        
    def fill(self):
        for i in range(8):
            self.write_all(DIGIT0+i, 0b11111111)
    
    def empty(self):
        for i in range(8):
            self.write_all(DIGIT0+i, 0b00000000)
    
    def intensity(self, i):
        if 0 <= i <= 15:
            self.write_all(INTENSITY, i)
    
    def on(self):
        self.write_all(SHUTDOWN, 0x1)
    
    def off(self):
        self.write_all(SHUTDOWN, 0x0)
        

# ==========
from machine import SPI
from machine import Pin
from time import sleep

hspi = SPI(1)
cs = Pin(33)

m = Max7219LEDMatrix(hspi, cs, 2)

m.fill()
sleep(0.5)

m.empty()
sleep(0.5)

m.intensity(0)
lines = (
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0),
    (0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0),
    (0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0),
    (0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
m.write_image(lines)
for _ in range(2):
    for i in range(16):
        m.intensity(i)
        sleep(0.1)
    for i in range(15, -1, -1):
        m.intensity(i)
        sleep(0.1)

m.empty()
sleep(0.5)

m.test(1)
sleep(0.3)
m.test(0)
sleep(0.3)

m.intensity(0)
lines = (
    (1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0),
    (1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0),
    (1,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0),
    (1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1),
    (1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1),
    (1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0))
m.write_image(lines)
sleep(2)

for _ in range(5):
    m.on()
    sleep(0.3)
    m.off()
    sleep(0.3)
    

        
    
    
                
            
            
            


