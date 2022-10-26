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


def init_perl_state(config, perl, load):
    data = config.read_perl_config(load)
    perl.screen.intensity(2, data["intensity"]["screen"])
    perl.timer.intensity(2, data["intensity"]["timer"])
    perl.scorer.intensity(2, data["intensity"]["scorer"])
    perl.buzzer.mute = data["mute"]


def save_perl_state(config, perl, dump, sleep_ms, randint):
    config.write_perl_config(perl, dump)
    flip_led_tubes(perl.timer, "SAUE", sleep_ms, randint)
    flip_led_tubes(perl.scorer, "SUCC", sleep_ms, randint)


def restore_perl_state(config, perl, dump, load, sleep_ms, randint):
    config.write_perl_config(perl, dump, restore=True)
    init_perl_state(config, perl, load)
    flip_led_tubes(perl.timer, "SEt ", sleep_ms, randint)
    flip_led_tubes(perl.scorer, "dEF ", sleep_ms, randint)
    

def update_buzzer(perl, mute, sleep_ms, randint):
    perl.buzzer.mute = mute
    if not mute:
        flip_led_tubes(perl.scorer, "On  ", sleep_ms, randint)
    elif mute:
        flip_led_tubes(perl.scorer, "OFF ", sleep_ms, randint)

