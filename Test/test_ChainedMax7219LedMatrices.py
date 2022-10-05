# Hardware driver of daisy chained LED matrices with max7219
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

class ChainedMax7219Matrices:
    def __init__(self, spi, cs, num):
        # spi (machine.SPI): serial phripheral interface
        # cs (machine.Pin): chip select pin
        # num (integer greater than 0): number of daisy-chained 8*8 LED matrix
        # slice (tuple): for split a row of data into several lists with 8 elements
        self.spi = spi
        self.cs = cs
        self.num = num
        self.slice = tuple((i*8, i*8+8) for i in range(num))
        self._init()


    def _init(self):
        # initialize SPI, CS and registers.
        self.spi.init(baudrate=900000, polarity=0, phase=0, firstbit=self.spi.MSB)
        self.cs.init(mode=Pin.OUT, drive=Pin.DRIVE_0)
        self.switch(1)
        self.test(0)
        self.intensity(6)
        self.writeall(SCANLIMIT, 0x7)
        self.writeall(DECODEMODE, 0x0)
        self.clear() # make sure every LED is initially turned off


    def writeall(self, addr, data):
        # write same addr+data into register of every max7219 
        self.cs.off()
        for _ in range(self.num):
            self.spi.write(bytearray([addr, data]))
        self.cs.on()


    def writerow(self, row, data):
        # write data for one row
        # row: an integer in interval [0, 7] represents the index of row
        # data: a tuple or list with length of 8*self.num, each element is 0 or 1.
        self.cs.off()
        for n in range(self.num):
            self.spi.write(bytearray([DIGIT0+row,\
            eval("0b{}{}{}{}{}{}{}{}".format(*data[self.slice[n][0]:self.slice[n][1]]))]))
        self.cs.on()


    def fill(self, *rows):
        # every element in rows should in interval [0, 7]
        if not rows:
            rows = (i for i in range(8))
        for r in rows:
            self.writeall(DIGIT0+r, 0b11111111)


    def clear(self, *rows):
        # every element in rows should in interval [0, 7]
        if not rows:
            rows = (i for i in range(8))
        for r in rows:
            self.writeall(DIGIT0+r, 0b00000000)


    def test(self, on):
        if on == 1:
            self.writeall(DISPLAYTEST, 0x1)
        elif on == 0:
            self.writeall(DISPLAYTEST, 0x0)


    def intensity(self, i):
        if 0 <= i <= 15:
            self.writeall(INTENSITY, i)


    def switch(self, state):
        if state == 1:
            # switch on
            self.writeall(SHUTDOWN, 0x1)
        elif state == 0:
            # switch off
            self.writeall(SHUTDOWN, 0x0)



# ==========
from machine import SPI
from machine import Pin
from time import sleep

hspi = SPI(1)
cs = Pin(33)

m = ChainedMax7219Matrices(hspi, cs, 2)

m.fill()
sleep(0.5)

m.clear(0, 2, 4, 6)
sleep(0.5)

m.clear()

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
for r in range(len(lines)):
    m.writerow(r, lines[r])
for _ in range(2):
    for i in range(16):
        m.intensity(i)
        sleep(0.1)
    for i in range(15, -1, -1):
        m.intensity(i)
        sleep(0.1)

m.clear()
sleep(0.5)

rows = (
    (1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0),
    (0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1)
    )
for i in range(8):
    m.writerow(i, rows[i%2])
    sleep(0.1)
    m.writerow(i, (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
for i in range(8):
    m.writerow(i, rows[i%2])
    sleep(0.1)
    m.writerow(i, (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))

m.clear()
sleep(0.5)

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
for r in range(len(lines)):
    m.writerow(r, lines[r])
sleep(2)

for _ in range(5):
    m.switch(1)
    sleep(0.3)
    m.switch(0)
    sleep(0.3)

m.switch(1)
m.clear()
m.fill(1,3,5,7)
sleep(0.5)
m.clear(1,3,5,7)
sleep(0.5)

m.test(1)
sleep(0.3)
m.test(0)
sleep(0.3)