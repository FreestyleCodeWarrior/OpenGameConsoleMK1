# Entry point of the system of Open Game Consule
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

from machine import Pin
from machine import SPI
from machine import SoftI2C
from machine import Timer

from drivers.max7219 import LedMatrix
from drivers.tm1650 import LedDigitalTube
from drivers.buttons import Buttons
from drivers.buzzer import Buzzer

from constant import HardwareID
from peripheral import Peripheral

from time import sleep

if __name__ == "__main__":
    p = Peripheral(HardwareID, LedMatrix, LedDigitalTube, Buzzer, Buttons, SPI, SoftI2C, Pin, Timer)
    p.screen.test(1)
    p.timer.digits("1234")
    p.scorer.digits("5678")
    p.buzzer.buzz(1000)
    sleep(1)
    p.screen.test(0)
    p.timer.digits("    ")
    p.scorer.digits("    ")