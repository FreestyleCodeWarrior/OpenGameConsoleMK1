# Hardware driver of discrete LED matrices with max7219
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

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

class DiscreteMax7219Matrices:
    def __init__(self, spi, cs_pins):
        self.spi = spi
        self.cs_pins = cs_pins
        self._init()
    
    def _init(self):
        self.spi.init(baudrate=900000, polarity=0, phase=0, firstbit=self.spi.MSB)
        for cs_pin in self.cs_pins:
            cs_pin.init(mode=Pin.OUT, drive=Pin.DRIVE_0)
        self.switch(1)
        self.test(0)
        self.intensity(6)
        self._writeall(SCANLIMIT, 0x7)
        self._writeall(DECODEMODE, 0x0)
        for i in range(8):
            self._writeall(DIGIT0+i, 0b00000000)

    def _writeall(self, addr, data):
        for cs_pin in self.cs_pins:
            cs_pin.off()
        self.spi.write(bytearray([addr, data]))
        for cs_pin in self.cs_pins:
            cs_pin.on()
    
    def writerow(self, cs_index, row_index, data):
        self.cs_pins[cs_index].off()
        self.spi.write(bytearray([DIGIT0+row_index, data]))
        self.cs_pins[cs_index].on()
    
    def clear(self):
        for i in range(8):
            self._writeall(DIGIT0+i, 0b00000000)
    
    def test(self, on):
        if on == 1:
            self._writeall(DISPLAYTEST, 0x1)
        elif on == 0:
            self._writeall(DISPLAYTEST, 0x0)

    def intensity(self, i):
        if 0 <= i <= 15:
            self._writeall(INTENSITY, i)
    
    def switch(self, state):
        if state == 1:
            # switch on
            self._writeall(SHUTDOWN, 0x1)
        elif state == 0:
            # switch off
            self._writeall(SHUTDOWN, 0x0)

#======
from machine import SPI
from machine import Pin
from time import sleep

hspi = SPI(1)
cs_pins = [Pin(32), Pin(33)]

m = DiscreteMax7219Matrices(hspi, cs_pins)
m.test(1)
sleep(1)
m.test(0)
sleep(1)

datalines = (
   (0b00011000,
    0b00111100,
    0b01100110,
    0b01100110,
    0b01100110,
    0b01111110,
    0b01100110,
    0b01100110),
    
   (0b01111100,
    0b01100110,
    0b01100110,
    0b01111100,
    0b01111110,
    0b01100110,
    0b01100110,
    0b01111100))

m.intensity(0)
for i in range(2):
    for x in range(8):
        m.writerow(i, x, datalines[i][x])
sleep(1)

for _ in range(2):
    for i in range(16):
        m.intensity(i)
        sleep(0.05)
    for i in range(15,-1,-1):
        m.intensity(i)
        sleep(0.05)

for i in range(5):
    m.switch(0)
    sleep(0.3)
    m.switch(1)
    sleep(0.3)

sleep(1)
m.clear()
sleep(1)

line = [0,0,0,0,0,0,0,0]
for x in range(2):
    for y in range(8):
        data = [0,0,0,0,0,0,0,0]
        if x == 1:
            y = [7,6,5,4,3,2,1,0][y]
        data[y] = 1
        m.writerow(x,y,eval("0b{}{}{}{}{}{}{}{}".format(*data)))
        sleep(0.2)
        m.writerow(x,y,0b00000000)

sleep(1)
m.clear()


        
        
        
        
        