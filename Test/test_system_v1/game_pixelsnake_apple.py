from random import randint
from time import ticks_ms


class Apples:
    def __init__(self):
        self.coords = {}
    
    
    def place(self, snake_body):
        coord = (randint(0, 7), randint(0, 15))
        while (coord in snake_body) or (coord in self.coords):
            coord = (randint(0, 7), randint(0, 15))
        self.coords[(coord[0], coord[1])] = ticks_ms()
        return coord


    def remove(self, coord):
        del self.coords(coord)
