from game_pixelsnake_scorer import Scorer
from game_pixelsnake_snake import Snake
from game_pixelsnake_apple import Apple
from game_pixelsnake_functions import *
from game_timer import GameTimer
from time import sleep_ms


def run(perl, pages):
    game_scorer = Scorer()
    game_timer = set_game_timer(GameTimer, perl, "Pixel Snake")
    snake = get_snake(Snake, perl)
    apple = Apple()
    game_start(perl, snake, game_timer)
    while not game_timer.game_over:
        if game_timer.game_pause:
            sleep_ms(100)
            continue
        update_snake(perl, snake, apple, game_scorer)
        if is_body_crashed(snake) or is_edge_crashed(snake):
            over_game(perl, game_timer)
            continue
        place_apple(perl, apple, snake)
        perl.screen.refresh()
        sleep_ms(100 if snake.ac_state else 300)
        snake.accelerate(False)
    save_game_record("Pixel Snake", game_timer, game_scorer)
    pages.game_select(0)
            
            
            