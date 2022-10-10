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

SETTING = const(0b01001000) # command for display settings
POWERON = const(1) # power on led segments
POWEROFF = const(0) # power off led segments

# seven-segment mode: 1
# eight_segment mode: 0
SEGNUM = {7:1, 8:0}

# mapping of single character and display content
ENCODE = {
    " ":0,
    "0":63,
    "1":6,
    "2":91,
    "3":79,
    "4":102,
    "5":109,
    "6":125,
    "7":7,
    "8":127,
    "9":111,
    ".":128,
    "0.":191,
    "1.":134,
    "2.":219,
    "3.":207,
    "4.":230,
    "5.":237,
    "6.":125,
    "7.":135,
    "8.":255,
    "9.":239,
    }

class Tm1650NumericLedSegments:
    def __init__(self, si2c, init_intensity, segnum):
        self.si2c = si2c
        self._intensity = INT[init_intensity]
        self._segnum = SEGNUM[segnum]
        self._state = POWERON
        self._set()
        self.clear()
    
    def _write(self, byte_1, byte_2):
        self.si2c.start()
        self.si2c.write(bytearray([byte_1, byte_2]))
        self.si2c.stop()
    
    def _set(self):
        self._write(SETTING,\
        eval("0b0{}{}{}{}00{}".format(*self._intensity, self._segnum, self._state)))
    
    def digits(self, nums):
        for i in range(4):
            self._write(DIG[i], ENCODE[nums[i]])
        
    def digit(self, pos, num):
        self._write(DIG[pos], ENCODE[num])
    
    def draw(self, pos, data):
        self._write(DIG[pos], data)
    
    def clear(self):
        for i in range(4):
            self._write(DIG[i], 0)
    
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
t = Tm1650NumericLedSegments(i2c, 0, 8)

t.digits('1234')
sleep(1)
t.clear()
sleep(1)

t.digits('5678')
sleep(1)

t.digit(2, "5")
sleep(1)

for i in range(1,5):
    t.draw(i-1, i)
sleep(1)

t.digits("8888")
for i in range(8):
    t.intensity(i)
    sleep(0.1)
for i in range(7,-1,-1):
    t.intensity(i)
    sleep(0.1)

for i in range(6):
    t.switch(i%2)
    sleep(0.2)
t.clear()

t.digit(1,".")
sleep(1)
t.clear()