# Entry point of the system of Open Game Consule
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32


from peripheral import Peripheral
from pages import Pages
import functions

from time import sleep

if __name__ == "__main__":
    p = Peripheral()
    p.screen.test(1)
    p.timer.chars("8888")
    p.scorer.chars("8888")
    #p.buzzer.buzz(100)
    sleep(0.1)
    p.screen.test(0)
    p.timer.chars("    ")
    p.scorer.chars("    ")
    
    functions.init_perl_state(p)
    pages = Pages(p)
    p.buttons.start(100)
    
    
    