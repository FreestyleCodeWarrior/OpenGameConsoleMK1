# Functions used to call methods of objects
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

def init_perl_state(Setting, perl, json):
    info = Setting(json).info
    perl.screen.intensity(2, info["general"]["intensity"]["screen"])
    perl.timer.intensity(2, info["general"]["intensity"]["timer"])
    perl.scorer.intensity(2, info["general"]["intensity"]["scorer"])
    perl.buzzer.switch(info["general"]["sound"])


def save_perl_state(Setting, perl, json):
    setting = Setting(json)
    setting.info["general"]["intensity"]["screen"] = perl.screen._intensity
    setting.info["general"]["intensity"]["timer"] = perl.timer._intensity
    setting.info["general"]["intensity"]["scorer"] = perl.scorer._intensity
    setting.info["general"]["sound"] = 1 if not perl.buzzer.mute else 0
    setting.save()
    perl.timer.chars("SAUE")
    perl.scorer.chars("SUCC")


def default_perl_state(Setting, perl, json):
    Setting(json).default()
    init_perl_state(Setting, perl, json)
    perl.timer.chars("SEt ")
    perl.scorer.chars("dEF ")
    

def update_buzzer(perl, state):
        perl.buzzer.switch(state)
        if state == 1:
            perl.scorer.chars("On  ")
        elif state == 0:
            perl.scorer.chars("OFF  ")



    