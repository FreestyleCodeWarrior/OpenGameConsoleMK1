from machine import Timer
from game_pixelsnake_scorer import Scorer
from game_pixelsnake_snake import Snake
from game_pixelsnake_apple import Apple
from game_pixelsnake_functions import *
from game_functions import *
from game_timer import GameTimer


class GameFlow:
    def __init__(self, perl):
        self.perl = perl
        
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
        

    def begin(self, resume=False):
        if not resume:
            start_game(self.perl, self.button_events, self.game_timer, self.game_scorer)
        self.timer.init(mode=Timer.PERIODIC, period=self.clock_period, callback=self.refresh)
        

    def refresh(self, _):
        if self.game_timer.game_over:
            self.clock.deinit()
            self.end()
            return None
        elif self.game_timer.game_pause:
            self.clock.deinit()
            return None
        if update_snake(self.perl, self):
            over_game(self)
        place_apple(self.perl, self.apple, self.snake)
        perl.screen.refresh()


    def end(self, _):
        save_game_record("Pixel Snake", self.game_timer, self.game_scorer)
        pages.game_select(0)




