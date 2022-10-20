# Functions used to call methods of objects
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

def init_perl_state(Setting, Filename, perl, json):
    info = Setting(json, Filename()).info
    perl.screen.intensity(info["general"]["intensity"]["screen"])
    perl.timer.intensity(info["general"]["intensity"]["timer"])
    perl.scorer.intensity(info["general"]["intensity"]["scorer"])
    perl.buzzer.switch(info["general"]["sound"])
    