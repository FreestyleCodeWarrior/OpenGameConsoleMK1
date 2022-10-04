# simple demonstration of flowing lines on led metrix
# ESP32-WROOM-32
# max7219 MSB First

from machine import SPI
from machine import Pin
from time import sleep

hspi = SPI(1, baudrate=800000, polarity=0, phase=0, firstbit=SPI.MSB)
cs = Pin(33, Pin.OUT, drive=Pin.DRIVE_0)

for i in range(1,9):
    cs.value(0)
    hspi.write(bytearray([i, 0x0]))
    cs.value(1)
    
for i in range(1,9):
    cs.value(0)
    hspi.write(bytearray([i, 0x0]))
    cs.value(1)


# no decode
cs.value(0)
hspi.write(bytearray([0x9, 0x0]))
cs.value(1)

# lowest intensity
cs.value(0)
hspi.write(bytearray([0xA, 0x1]))
cs.value(1)

# set scan limit for 8x8 matrix
cs.value(0)
hspi.write(bytearray([0xB, 0x7]))
cs.value(1)

# normal operation mode
cs.value(0)
hspi.write(bytearray([0xC, 0x1]))
cs.value(1)

# turn off test mode
cs.value(0)
hspi.write(bytearray([0xF, 0x0]))
cs.value(1)

# turn on all leds on the first row
"""
cs.value(0)
hspi.write(bytearray([3, 0xFF]))
cs.value(1)
cs.value(0)
hspi.write(bytearray([0x2, 0xFF]))
cs.value(1)
"""
for i in range(1):
    for i in range(1,9):
        cs.value(0)
        hspi.write(bytearray([i,0xFF]))
        cs.value(1)
        sleep(0.2)
        
        cs.value(0)
        hspi.write(bytearray([i, 0x0]))
        cs.value(1)
        sleep(0.2)

cs.value(0)
for i in range(2):
    hspi.write(bytearray([0xF,0x1]))
cs.value(1)

sleep(1)

cs.value(0)
for i in range(2):
    hspi.write(bytearray([0xF,0x0]))
cs.value(1)

sleep(1)

# shutdown
cs.value(0)
hspi.write(bytearray([0xC, 0x0]))
hspi.write(bytearray([0xC, 0x0]))
cs.value(1)


    