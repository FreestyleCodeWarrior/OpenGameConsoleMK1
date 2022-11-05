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
        self.snake = Snake()
        self.apple = Apple()
        self.clock = Timer(3)
        
        self.init_disp_info = self.snake.body
        self.clock_period = 300
        self.button_events = (("up", self.snake.turn, ("u",)),
                           ("down", self.snake.turn, ("d",)),
                           ("left", self.snake.turn, ("l",)),
                           ("right", self.snake.turn, ("r",)))
        
        if self.game_timer.time_limit:
            self.refresh = self.refresh_countdown
        else:
            self.refresh = self.refresh_normal
    
    
    def refresh_normal(self, _):
        if update_snake(self.perl, self.snake, self.apple, self.game_scorer):
            stop_game(self.perl, self, self.pages, "over")
        place_apple(self.perl, self.snake, self.apple)
        self.perl.screen.refresh()


    def refresh_countdown(self, _):
        if update_snake(self.perl, self.snake, self.apple, self.game_scorer):
            stop_game(self.perl, self, self.pages, "over")
        place_apple(self.perl, self.snake, self.apple)
        self.perl.screen.refresh()
        if self.game_timer.game_over:
            stop_game(self.perl, self, self.pages, "over")



