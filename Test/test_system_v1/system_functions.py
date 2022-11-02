from time import sleep_ms
from random import randint
from machine import Timer

import system_configurator as sys_config
import game_configurator as game_config


def flip_screen(screen, rows, cs):
    for m in range(2):
        for n in range(8):
            screen.directrow(cs, n+1, 255 if m==0 else rows[n])
            sleep_ms(20)


def blink_screen(perl, time, on_duration, off_duration):
    for _ in range(time):
        perl.screen.switch(0)
        sleep_ms(off_duration)
        perl.screen.switch(1)
        sleep_ms(on_duration)


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
    data = sys_config.read_perl_config()
    perl.screen.intensity(2, data["intensity"]["screen"])
    perl.timer.intensity(2, data["intensity"]["timer"])
    perl.scorer.intensity(2, data["intensity"]["scorer"])
    perl.buzzer.mute = data["mute"]


def save_perl_state(perl):
    sys_config.write_perl_config(perl)
    flip_led_tubes(perl.timer, "SAUE")
    flip_led_tubes(perl.scorer, "SUCC")


def restore_perl_state(perl):
    sys_config.write_perl_config(perl, restore=True)
    init_perl_state(perl)
    flip_led_tubes(perl.timer, "SEt ")
    flip_led_tubes(perl.scorer, "dEF ")


def clear_game_data(perl, game_name):
    config_game_data(game_name, "score records", [])
    flip_led_tubes(perl.timer, "CLr ")
    flip_led_tubes(perl.scorer, "SUCC")


def get_game_data(game_name, key):
    data = game_config.read_game_data(game_name)
    if isinstance(key, str):
        return data[key]
    elif isinstance(key, tuple):
        return tuple((data[k] for k in key))


def config_game_data(game_name, key, value):
    data = game_config.read_game_data(game_name)
    data[key] = value
    game_config.write_game_data(game_name, data)


def update_game_timer(perl, game_name, seconds):
    if not seconds:
        config_game_data(game_name, "time limit", 0)
        config_game_data(game_name, "countdown", False)
        flip_led_tubes(perl.timer, "SEt ")
        flip_led_tubes(perl.scorer, "dEF ")
    else:
        config_game_data(game_name, "time limit", seconds)
        flip_led_tubes(perl.timer, "SAUE")
        flip_led_tubes(perl.scorer, "SUCC")


def update_buzzer(perl, mute):
    perl.buzzer.mute = mute
    if not mute:
        flip_led_tubes(perl.scorer, "On  ")
    elif mute:
        flip_led_tubes(perl.scorer, "OFF ")

