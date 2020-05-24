#! usr/bin/env/ python3
# config.py
# coded by Saito-Saito-Saito
# last edited 24 May 2020

import logging

logging.basicConfig(level=logging.CRITICAL, format='%(filename)s - %(lineno)d - %(levelname)s - %(message)s')

# board size = SIZE * SIZE
SIZE = 4

# if the square has no number, record as 0
EMPTY = 0

# directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# the probability of appearing 4
FOUR_PROBABILITY = 1 / 8

# game status
GAME_PRC = 0
GAME_CLR = 1
GAME_OVR = -1

DEFAULT_GOAL = 32

# for return
SUCCEEDED = True
FAILED = False
ERROR = -1
