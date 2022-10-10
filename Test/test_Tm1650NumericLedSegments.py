# Hardware driver of numeric LED segments with tm1650
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

from micropython import const

# Addresses of digit display unit
DIG = (
    const(0x68),
    const(0x6a),
    const(0x6c),
    const(0x6e)
    )

# Levels of intensity
INT = (
    const((0,0,1)),
    const((0,1,0)),
    const((0,1,1)),
    const((1,0,0)),
    const((1,0,1)),
    const((1,1,0)),
    const((1,1,1)),
    const((0,0,0))
    )

SETTING = const(0b01001000) # Command for display settings
POWERON = const(1) # power on led segments
POWEROFF = const(0) # power off led segments

# seven-segment mode: 1
# eight_segment mode: 0
SEGNUM = const({7:1, 8:0})


class Tm1650NumericLedSegments:
    def __init__(self, si2c, init_intensity, segnum):
        self.si2c = si2c
        self._intensity = INT[init_intensity]
        self._segnum = SEGNUM[segnum]
        self._state = POWERON
        self._set()
    
    def _write(self, byte_1, byte_2):
        self.si2c.start()
        self.si2c.write(bytearray([byte_1, byte_2]))
        self.si2c.stop()
    
    def _set(self):
        self._write(SETTING,\
        eval("0b0{}{}{}{}00{}".format(*self._intensity, self._segnum, self._state)))
    
    def number(self, number):
        pass
    
    def intensity(self, i):
        self._intensity = INT[i]
        self._set()
    
    def switch(self, state):
        self._state = state
        self._set()


from machine import SoftI2C
from machine import Pin
from time import sleep

i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.start()
i2c.write(bytearray([0b01001000,0b00010001]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00000001]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00000010]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00000100]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00001000]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00010000]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00100000]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b01000000]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b11111111]))
i2c.stop()
"""