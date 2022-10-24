# Functions used to call methods of objects
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32


def flip_screen(screen, rows, cs, sleep_ms):
    for m in range(2):
        for n in range(8):
            screen.directrow(cs, n+1, 255 if m==0 else rows[n])
            sleep_ms(20)


def flip_led_tubes(driver, characters, sleep_ms, randint):
    for _ in range(10):
        driver.segments(tuple(randint(1,255) for _ in range(4)))
        sleep_ms(20)
    driver.chars(characters)


def init_perl_state(Setting, perl, json):
    info = Setting(json).info
    perl.screen.intensity(2, info["general"]["intensity"]["screen"])
    perl.timer.intensity(2, info["general"]["intensity"]["timer"])
    perl.scorer.intensity(2, info["general"]["intensity"]["scorer"])
    perl.buzzer.switch(info["general"]["sound"])


def save_perl_state(Setting, perl, json, sleep_ms, randint):
    setting = Setting(json)
    setting.info["general"]["intensity"]["screen"] = perl.screen._intensity
    setting.info["general"]["intensity"]["timer"] = perl.timer._intensity
    setting.info["general"]["intensity"]["scorer"] = perl.scorer._intensity
    setting.info["general"]["sound"] = 1 if not perl.buzzer.mute else 0
    setting.save()
    flip_led_tubes(perl.timer, "SAUE", sleep_ms, randint)
    flip_led_tubes(perl.scorer, "SUCC", sleep_ms, randint)


def default_perl_state(Setting, perl, json, sleep_ms, randint):
    Setting(json).default()
    init_perl_state(Setting, perl, json)
    flip_led_tubes(perl.timer, "SEt ", sleep_ms, randint)
    flip_led_tubes(perl.scorer, "dEF ", sleep_ms, randint)
    

def update_buzzer(perl, state, sleep_ms, randint):
        perl.buzzer.switch(state)
        if state == 1:
            flip_led_tubes(perl.scorer, "On  ", sleep_ms, randint)
        elif state == 0:
            flip_led_tubes(perl.scorer, "OFF ", sleep_ms, randint)

