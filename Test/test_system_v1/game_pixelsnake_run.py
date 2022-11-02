from game_pixelsnake_scorer import Scorer
from game_pixelsnake_snake import Snake
from game_pixelsnake_apple import Apple
from game_timer import GameTimer
from time import sleep_ms
import game_pixelsnake_functions as funcs


def run(perl):
    game_scorer = Scorer()
    game_timer = funcs.set_game_timer(GameTimer, perl, "Pixel Snake")
    snake = funcs.get_snake(Snake, perl)
    apple = Apple()
    funcs.notice(perl, "start")
    funcs.bind_button_events(perl, "start", snake, game_timer)
    while not game_timer.game_over:
        if game_timer.game_pause:
            sleep_ms(100)
            continue
        funcs.update_snake
        
            
    
    
    
    
    print("Pixel Snake - Initiated")
    