from time import sleep_ms
from system_functions import roll_led_tubes
from system_functions import flip_led_tubes
from system_functions import blink_screen
from system_functions import get_game_data
from system_functions import config_game_data


def notice(perl, mode, game_flow=None):
    if mode == "start":
        blink_screen(perl, 3, 50, 100)
        flip_led_tubes(perl.timer, "3333")
        flip_led_tubes(perl.scorer, "3333")
        for i in range(3, 0, -1):
            perl.timer.chars(str(i) * 4)
            perl.scorer.chars(str(i) * 4)
            sleep_ms(1000)
        for _ in range(3):
            perl.timer.chars("GOGO")
            perl.scorer.chars("GOGO")
            sleep_ms(300)
            perl.timer.chars("    ")
            perl.scorer.chars("    ")
            sleep_ms(100)
    elif mode == "over":
        blink_screen(perl, 3, 200, 150)
        flip_led_tubes(perl.timer, "GAME")
        perl.timer.segmode("8")
        flip_led_tubes(perl.scorer, "OvEr")
    elif mode == "pause":
        flip_led_tubes(perl.timer, "GAME")
        perl.timer.segmode("8")
        flip_led_tubes(perl.scorer, "StOP")
    elif mode == "resume":
        flip_led_tubes(perl.timer, game_flow.game_timer.encoded_seconds)
        perl.timer.segmode("7")
        flip_led_tubes(perl.scorer, game_flow.game_scorer.encoded_score)
        
        
def bind_button_events(perl, mode, game_flow=None):
    perl.buttons.handlers = {}
    if mode == "start":
        for event in game_flow.button_events:
            perl.buttons.assign(event[0], event[1], event[2])
        perl.buttons.assign("back", pause_game, (perl, game_flow))
    elif mode == "pause":
        perl.buttons.assign("ok", resume_game, (perl, game_flow))
        perl.buttons.assign("back", quit_game, (game_flow,))
    elif mode == "over":
        perl.buttons.assign("ok", notice, (perl, "resume", game_flow))
        perl.buttons.assign("back", quit_game, (game_flow,))


def start_game(perl, game_flow):
    roll_led_tubes(start=False)
    notice(perl, "start")
    game_flow.game_timer.start()
    game_flow.game_scorer.show()
    bind_button_events(perl, "start", game_flow)


def pause_game(perl, game_flow):
    game_flow.game_timer.interrupt("pause")
    notice(perl, "pause")
    bind_button_events(perl, "pause", game_flow)


def resume_game(perl, game_flow):
    game_flow.game_timer.interrupt("resume")
    notice(perl, "resume", game_flow)
    bind_button_events(perl, "start", game_flow)
    game_flow.begin(resume=True)


def over_game(perl, game_flow):
    game_flow.game_timer.interrupt("pause")
    notice(perl, "over")
    bind_button_events(perl, "over", game_flow)


def quit_game(game_flow):
    game_flow.game_timer.interrupt("quit")


def set_game_timer(GameTimer, perl, game_name):
    countdown, time_limit = get_game_data(game_name, ("countdown", "time limit"))
    return GameTimer(perl.timer, time_limit if countdown else None)


def save_game_record(game_name, game_timer, game_scorer):
    records = get_game_data(game_name, "score records")
    records.append([game_timer.get_seconds_used(), game_scorer.encoded_score])
    records.sort(key=lambda item: item[1], reverse=True)
    config_game_data(game_name, "score records", records)
