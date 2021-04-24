# Generating random numbers
import random
import secrets


def random_number():
    # random.seed(12)
    for roll in range(4):
        print(secrets.randbits(3), end=', ')


random_number()


def coin():
    for roll in range(6):

        print('H' if random.randrange(2) == 0 else 'T', end=', ')


coin()