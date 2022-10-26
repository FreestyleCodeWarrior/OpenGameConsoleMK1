# Entry point of the system of Open Game Consule
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32


from time import sleep_ms
from json import dump, load
from random import randint
from machine import Pin
from machine import SPI
from machine import SoftI2C
from machine import Timer

from drivers.max7219 import LedMatrix
from drivers.tm1650 import LedDigitalTube
from drivers.buttons import Buttons
from drivers.buzzer import Buzzer

import functions
import icons
import configurator
from peripheral import Peripheral
from page import Page

from time import sleep

if __name__ == "__main__":
    p = Peripheral(LedMatrix, LedDigitalTube, Buzzer, Buttons, SPI, SoftI2C, Pin, Timer)
    p.screen.test(1)
    p.timer.chars("8888")
    p.scorer.chars("8888")
    #p.buzzer.buzz(100)
    sleep(0.2)
    p.screen.test(0)
    p.timer.chars("    ")
    p.scorer.chars("    ")
    """
    functions.init_perl_state(configurator, p, load)
    page = Page(icons, p, functions, configurator, dump, load, sleep_ms, randint)
    p.buttons.start(100)
    """
    
    