import random

couriers = ["Al", "Bal", "Cal", "Mal"]


def introduce_chaos():
    random.shuffle(couriers)


def get_couriers():
    introduce_chaos()
    return couriers