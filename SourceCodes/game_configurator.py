from json import dump
from json import load


def get_filename(game_name):
    return "game_{}_config.json".format("".join(game_name.split()).lower())


def default_game_data():
    return {
        "countdown":False,
        "time limit":0,
        "score records":[]
        }


def read_game_data(game_name):
    try:
        file = open(get_filename(game_name), "r")
    except:
        write_game_data(game_name, default_game_data())
        return default_game_data()
    else:
        data = load(file)
        file.close()
        return data


def write_game_data(game_name, data):
    with open(get_filename(game_name), "w") as file:
        dump(data, file)