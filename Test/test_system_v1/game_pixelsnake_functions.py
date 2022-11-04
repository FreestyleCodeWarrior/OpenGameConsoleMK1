from system_functions import flip_screen
from game_functions import over_game
from system_icons import empty
from random import randint


def get_snake(Snake, perl):
    snake = Snake()
    flip_screen(perl.screen, empty(), 0)
    flip_screen(perl.screen, empty(), 1)
    perl.screen.pixels("1", snake.body)
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
       

def place_apple(perl, snake, apple):
    if randint(1,10) == 1:
        coord = apple.place(snake.body)
        perl.screen.pixels("1", (coord,))


def update_snake(perl, snake, apple):
    snake.move_head()
    if is_body_crashed(snake) or is_edge_crashed(snake):
        return True
    perl.screen.pixels("1", (snake.body[-1],))
    if snake.body[-1] in apple.coords:
        game_scorer.add(apple.coords[snake.body[-1]])
        game_scorer.show()
        apple.remove(snake.body[-1])
    else:
        perl.screen.pixels("0", (snake.move_tail(),))

        