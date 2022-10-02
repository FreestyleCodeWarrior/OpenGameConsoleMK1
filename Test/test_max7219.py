# max7219 MSB First
from machine import SPI
from machine import Pin
from time import sleep

hspi = SPI(1, baudrate=1000000, polarity=0, phase=0)
cs = Pin(15, Pin.OUT)
cs.value(0)
hspi.write(bytearray([0xC, 1]))
"""
for i in range(1,9):
    cs.value(1)
    hspi.write(bytearray([i,0]))
    cs.value(0)
    
for i in range(1,9):
    cs.value(1)
    hspi.write(bytearray([i,0]))
    cs.value(0)
"""
for i in range(1,9):
    cs.value(0)
    hspi.write(bytearray([1, i]))
    cs.value(1)
    sleep(0.2)
    cs.value(0)
    hspi.write(bytearray([1, i+1]))
    cs.value(1)
    sleep(0.2)
    print(i)

cs.value(0)
hspi.write(bytearray([0xC, 0]))
cs.value(1)
cs.value(0)
hspi.write(bytearray([0xC, 0]))
cs.value(1)


    