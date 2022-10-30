from json import dump
from json import load


def get_filename(game_name):
    return "game_{}_config.json".format("".join(game_name.split()).lower())


def default_game_config():
    return {
        "countdown":False,
        "time limit":0,
        "score records":[]
        }


def read_game_config(game):
    try:
        file = open(get_filename(game), "r")
    except:
        write_game_config(game, default_game_config())
        return default_game_config()
    else:
        data = load(file)
        file.close()
        return data


def write_game_config(game, data):
    with open(get_filename(game), "w") as file:
        dump(data, file)