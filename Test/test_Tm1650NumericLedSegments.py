# Hardware driver of numeric LED segments with tm1650
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

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
i2c.write(bytearray([0b01101000, 0b10000000]))
i2c.stop()

i2c.start()
i2c.write(bytearray([0b01101000, 0b00000000]))
i2c.stop()