from random import randint
from time import sleep_ms
from system_functions import flip_led_tubes


def player_get_ready(perl):
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


def bind_button_events(perl, mode, snake=None, game_timer=None):
    if mode == "clear":
        perl.button.handlers = {}
    elif mode == "start":
        perl.button.assigner("up", snake.turn, ("u",))
        perl.button.assigner("down", snake.turn, ("d",))
        perl.button.assigner("left", snake.turn, ("l",))
        perl.button.assigner("right", snake.turn, ("r",))
        perl.button.assigner("ok", snake.accelerate, (True,))
        perl.button.assigner("back", game_timer.interrupt, ("pause",))
    elif mode == "pause":
        perl.button.handlers = {}
        perl.button.assigner("ok", game_timer.interrupt, ("resume",))
        perl.button.assigner("back", game_timer.interrupt, ("quit",))
        

def is_apple_eaten(snake, apple):
    if snake.body in apple.coords:
        return True
    return False


def is_body_crashed(snake):
    if snake.body[-1] in snake.body[:-1]:
        return True
    return False


def is_edge_crashed(snake):
    if (snake.body[-1][0] < 0) or (snake.body[-1][0] > 7) or \
       (snake.body[-1][1] < 0) or (snake.body[-1][1] > 15):
        return True
    return False
       

def place_apple(apple, snake, screen_driver):
    if randint(1,10) == 1:
        coord = apple.place(snake.body)
        screen_driver.pixels("1", (coord,))


def update_snake(snake, apple):
    snake.move(is_apple_eaten(snake.body, apple.coords))
        