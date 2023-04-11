import json


def write(dict, file):
    with open(file, "w") as file:
        json.dump(dict, file)


def read(file):
    with open(file, "r") as file:
        return json.load(file)
