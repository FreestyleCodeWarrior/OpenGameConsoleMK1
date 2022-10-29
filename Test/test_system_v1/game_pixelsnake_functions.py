from random import randint


def is_apple_eaten(snake_body, apple_coords):
    if snake_body in apple_coords:
        return True
    return False


def is_body_crashed(snake_body):
    if snake_body[-1] in snake_body[:-1]:
        return True
    return False


def is_edge_crashed(snake_body):
    if (snake_body[-1][0] < 0) or (snake_body[-1][0] > 7) or \
       (snake_body[-1][1] < 0) or (snake_body[-1][1] > 15):
        return True
    return False
       

def place_apple(apple, snake_body, screen_driver):
    if randint(1,10) == 1:
        coord = apple.place(snake_body)
        screen_driver.pixels("1", (coord,))


def update_snake(snake, apple_coords):
    snake.move(is_apple_eaten(snake.body, apple_coords))
        