# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32


from system_peripheral import Peripheral
from system_pages import Pages
import system_functions as funcs

from time import sleep


if __name__ == "__main__":
    perl = Peripheral()
    pages = Pages(perl)
    funcs.init_perl_state(perl)
    perl.buttons.start(100)
    
    
    
    
    