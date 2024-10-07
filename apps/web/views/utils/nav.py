import json


def nav():
    f = open(file="data/nav.json")
    nav = json.load(f)
    nav = nav["nav_core"]
    f.close()

    return nav
