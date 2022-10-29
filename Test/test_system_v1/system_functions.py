from time import sleep_ms
from random import randint
from machine import Timer

import system_configurator as config


def flip_screen(screen, rows, cs):
    for m in range(2):
        for n in range(8):
            screen.directrow(cs, n+1, 255 if m==0 else rows[n])
            sleep_ms(20)


def flip_led_tubes(driver, characters):
    for _ in range(10):
        driver.segments(tuple(randint(1,255) for _ in range(4)))
        sleep_ms(20)
    driver.chars(characters)


def roll_led_tubes(driver=None, characters=None, start=True):
    if start:
        global i
        i = 0
        def show(_):
            global i
            if i < len(characters)-3:
                driver.chars(characters[i:i+4])
                i += 1
            elif i < len(characters):
                driver.chars(characters[i:i+4]+characters[:4-(len(characters)-i)])
                i += 1
            else:
                i = 0
        Timer(2).init(mode=Timer.PERIODIC, period=150, callback=show)
    else:
        Timer(2).deinit()
        


def init_perl_state(perl):
    data = config.read_perl_config()
    perl.screen.intensity(2, data["intensity"]["screen"])
    perl.timer.intensity(2, data["intensity"]["timer"])
    perl.scorer.intensity(2, data["intensity"]["scorer"])
    perl.buzzer.mute = data["mute"]


def save_perl_state(perl):
    config.write_perl_config(perl)
    flip_led_tubes(perl.timer, "SAUE")
    flip_led_tubes(perl.scorer, "SUCC")


def restore_perl_state(perl):
    config.write_perl_config(perl, restore=True)
    init_perl_state(perl)
    flip_led_tubes(perl.timer, "SEt ")
    flip_led_tubes(perl.scorer, "dEF ")
    

def update_buzzer(perl, mute):
    perl.buzzer.mute = mute
    if not mute:
        flip_led_tubes(perl.scorer, "On  ")
    elif mute:
        flip_led_tubes(perl.scorer, "OFF ")

