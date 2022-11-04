from machine import Timer
from game_pixelsnake_scorer import Scorer
from game_pixelsnake_snake import Snake
from game_pixelsnake_apple import Apple
from game_pixelsnake_functions import *
from game_functions import *
from game_timer import GameTimer


class GameFlow:
    def __init__(self, perl, pages):
        self.perl = perl
        self.pages = pages
        
        self.game_scorer = Scorer(perl.scorer)
        self.game_timer = set_game_timer(GameTimer, perl, "Pixel Snake")
        self.snake = get_snake(Snake, perl)
        self.apple = Apple()
        self.clock = Timer(3)
        
        self.clock_period = 300
        self.button_events = (("up", self.snake.turn, ("u",)),
                           ("down", self.snake.turn, ("d",)),
                           ("left", self.snake.turn, ("l",)),
                           ("right", self.snake.turn, ("r",)))


    def refresh(self, _):
        if update_snake(self.perl, self.snake, self.apple):
            stop_game(self.perl, self, self.pages, "over")
        place_apple(self.perl, self.snake, self.apple)
        self.perl.screen.refresh()




