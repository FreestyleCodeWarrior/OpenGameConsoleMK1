from time import ticks_ms
from time import ticks_diff


class Scorer:
    def __init__(self, driver):
        self.driver = driver
        self.score = 0
        self.encode()


    def add(apple_time_tick):
        score = round(-0.01*ticks_diff(ticks_ms(), apple_time_tick)+100)
        if score > 0:
            self.score += score
        else:
            self.score += 1
    
    
    def encode(self):
        self.encoded_score = "{:0>4}".format(self.score)


    def show(self):
        self.encode()
        self.driver.chars(self.encoded_score)
