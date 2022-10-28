from time import ticks_ms
from time import ticks_diff


class Scorer:
    def __init__(self, driver):
        self.score = 0
        self.show()
    
    def add(apple_time_tick):
        score = round(-0.01*ticks_diff(ticks_ms(), apple_time_tick)+100)
        if score > 0:
            self.score += score
        else:
            self.score += 1
    
    def show():
        driver.chars("{:0>4}".format(self.score))
