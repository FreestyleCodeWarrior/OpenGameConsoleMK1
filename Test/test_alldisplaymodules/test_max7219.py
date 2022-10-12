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

class LedMatrix:
    def __init__(self, spi, cs_pins):
        # spi (machine.SPI): serial phripheral interface
        # cs_pins (tuple): elements of the tuple are instances of machine.Pin
        self.spi = spi
        self.cs_pins = cs_pins
        self.buffer = tuple(list("00000000") for _ in range(8*len(cs_pins)))
        self.changedrow = set()
        self._initpins()
        self._initsettings()
    
    def _initpins(self):
        self.spi.init(baudrate=10000000, polarity=0, phase=0, firstbit=self.spi.MSB)
        for cs_pin in self.cs_pins:
            cs_pin.init(mode=Pin.OUT, drive=Pin.DRIVE_0)
        
    def _initsettings(self):
        self.test(0)
        self.intensity(6)
        self._writeall(SCANLIMIT, 0x7)
        self._writeall(DECODEMODE, 0x0)
        self.clear()
        self.switch(1)

    def _writeall(self, addr, data):
        # write same data into each max7219
        for cs_pin in self.cs_pins:
            cs_pin.off()
        self.spi.write(bytearray([addr, data]))
        for cs_pin in self.cs_pins:
            cs_pin.on()
    
    def pixels(self, i, *coords):
        for x, y in coords:
            self.buffer[y][x] = i
            self.changedrow.add(y)
    
    def refresh(self):
        for y in self.changedrow:
            cs, row = divmod(y, 8)
            self.cs_pins[cs].off()
            self.spi.write(bytearray([row+1, eval("0b"+"".join(self.buffer[y]))]))
            self.cs_pins[cs].on()
        self.changedrow.clear()
    
    def writerow(self, row, data):
        # directly write the data 
        cs, row = divmod(row, 8)
        self.cs_pins[cs].off()
        self.spi.write(bytearray([row, data]))
        self.cs_pins[cs].on()
    
    def clear(self):
        # turn off every LED
        for i in range(8):
            self._writeall(DIGIT0+i, 0b00000000)
        self.buffer = tuple(list("00000000") for _ in range(8*len(cs_pins)))
    
    def test(self, on):
        if on == 1:
            self._writeall(DISPLAYTEST, 0x1)
        elif on == 0:
            self._writeall(DISPLAYTEST, 0x0)

    def intensity(self, i):
        if 0 <= i <= 15:
            self._writeall(INTENSITY, i)
    
    def switch(self, state):
        # turn on \ off the power supply to each LED
        if state == 1:
            # switch on
            self._writeall(SHUTDOWN, 0x1)
        elif state == 0:
            # switch off
            self._writeall(SHUTDOWN, 0x0)

#==============================================

from machine import SPI
from machine import Pin, freq
from time import sleep, ticks_diff, ticks_ms
from random import randint

freq(160000000)
m = LedMatrix(SPI(1), [Pin(32), Pin(33)])
for _ in range(10):
    ps = []
    for _ in range(20):
        t = (randint(0, 7), randint(0, 15))
        if t not in ps:
            ps.append(t)
    
    start = ticks_ms()
    m.pixels("1", *ps)
    m.refresh()
    a = ticks_diff(ticks_ms(), start)
    print(a)
    m.pixels("0", *ps)
    sleep(0.1)
    
m.clear()

