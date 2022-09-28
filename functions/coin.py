from random import random

# * Coin Toss!


def flip_coin():
    r = random()  # random() generates a number between 0 - 1 by default
    if r > 0.5:
        return "Off with their head!"
    else:
        return 'Off with their! uh ... Tail!'

# ? This is SHORTENED VERSION of flip_coin
# ? will actually OVERWRITE the previous version of flip_coin


def flip_coin():
    if random() > 0.5:
        return 'HEADS'
    else:
        return 'TAILS'


print(flip_coin())
