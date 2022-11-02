from random import randint
from time import sleep_ms
from system_functions import flip_led_tubes
from system_functions import flip_screen
from system_functions import blink_screen
from system_function import get_game_data
from system_icons import empty


def notice(perl, mode, game_timer=None):
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
        flip_led_tubes(perl.scorer, "OvEr")
    elif mode == "pause":
        flip_led_tubes(perl.timer, "GAME")
        flip_led_tubes(perl.scorer, "StOP")
    elif mode == "resume":
        flip_led_tubes(perl.timer, game_timer.encoded_seconds)
        flip_led_tubes(perl.scorer, game_scorer.encoded_score)
        
        
def bind_button_events(perl, mode, snake=None, game_timer=None):
    if mode == "clear":
        perl.button.handlers = {}
    elif mode == "start":
        perl.button.assigner("up", snake.turn, ("u",))
        perl.button.assigner("down", snake.turn, ("d",))
        perl.button.assigner("left", snake.turn, ("l",))
        perl.button.assigner("right", snake.turn, ("r",))
        perl.button.assigner("ok", snake.accelerate, (True,))
        perl.button.assigner("back", pause_game)
    elif mode == "pause":
        perl.button.handlers = {}
        perl.button.assigner("ok", resume_game)
        perl.button.assigner("back", game_timer.interrupt, ("quit",))


def pause_game(perl, game_timer):
    game_timer.interrupt("pause")
    notice(perl, "pause")
    bind_button_events(perl, "pause")


def resume_game(game_timer):
    pass


def quit_game():
    pass


def set_game_timer(GameTimer, perl, game_name):
    countdown, time_limit = get_game_data(game_name, ("countdown", "time limit"))
    return GameTimer(perl.timer, time_limit if countdown else None)


def get_snake(Snake, perl):
    snake = Snake()
    flip_screen(perl.screen, empty(), 0)
    flip_screen(perl.screen, empty(), 1)
    perl.screen.pixel("1", snake.body)
    perl.screen.refresh()
    return snake


def is_body_crashed(snake):
    if snake.body[-1] in snake.body[:-1]:
        return True
    return False


def is_edge_crashed(snake):
    if (snake.body[-1][0] < 0) or (snake.body[-1][0] > 7) or \
       (snake.body[-1][1] < 0) or (snake.body[-1][1] > 15):
        return True
    return False
       

def place_apple(perl, apple, snake):
    if randint(1,10) == 1:
        coord = apple.place(snake.body)
        perl.screen.pixels("1", (coord,))


def update_snake(perl, snake, apple, game_scorer):
    perl.screen.pixels("1", (snake.move_head(),))
    if snake.body[-1] in apple.coords:
        game_scorer.add(apple.coords[snake.body[-1]])
        game_scorer.show()
        apple.remove(snake.body[-1])
    else:
        perl.screen.pixels("0", (snake.move_tail(),))
        