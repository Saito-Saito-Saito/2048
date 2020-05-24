#! usr/bin/env/ Python3
# config.py
# coded by Saito-Saito-Saito
# last edited 24 May 2020

import copy
import random
import re

from config import *

class Board:
    def appear(self):
        for i in range(SIZE):
            if EMPTY in self.board[i]:
                break
        else:
            return False
        while True:
            col = random.randint(0, SIZE - 1)
            row = random.randint(0, SIZE - 1)
            if self.board[row][col] == EMPTY:
                # in case 4 appears
                if random.random() < FOUR_PROBABILITY:
                    self.board[row][col] = 4
                    logging.debug('4 appeared at {}, {}'.format(row, col))
                else:
                    self.board[row][col] = 2
                    logging.debug('2 appeared at {}, {}'.format(row, col))
                return True
            else:
                logging.debug('SELECTED THE SAME PLACE')

    def __init__(self, input_board=[], input_goal=DEFAULT_GOAL):
        if input_goal >= 100000:
            logging.warning('TOO BIG VALUE of input_goal')
            input_goal = DEFAULT_GOAL
        self.goal = input_goal
        if len(input_board) == SIZE:
            self.board = copy.deepcopy(input_board)
        else:
            self.board = [[EMPTY for col in range(SIZE)] for row in range(SIZE)]
        self.status = GAME_PRC
        self.appear()
        self.appear()

    def print(self):
        # print a border line
        print(' ', end='')
        for count in range(SIZE):
            print('--------', end='')
        # print \n
        print('')
        for row in range(SIZE):
            print('|', end='')
            for col in range(SIZE):
                if self.board[row][col] == EMPTY:
                    print('\t', end='|')
                else:
                    print(' {}'.format(self.board[row][col]).center(6) + '\t', end='|')
            # print \n
            print('\n ', end='')
            for count in range(SIZE):
                print('--------', end='')
            # print \n
            print('')

    def setcheck(self):
        # goal
        for row in range(SIZE):
            for col in range(SIZE):    
                if self.board[row][col] >= self.goal:
                    logging.info('GOAL at {}, {}'.format(row, col))
                    self.status = GAME_CLR
                    return GAME_CLR
        # no way to move
        subboard = Board(self.board, self.goal)
        if subboard.move(UP) == subboard.move(DOWN) == subboard.move(LEFT) == subboard.move(RIGHT) != SUCCEEDED:
            self.status = GAME_OVR
            return GAME_OVR
        # reaching here, it's not goal
        return GAME_PRC

    def move(self, direction):
        ever_moved = False
        # up
        if direction == UP:
            for col in range(SIZE):
                for row in range(SIZE):
                    ever_added = False
                    for focused_row in range(row + 1, SIZE):
                        # if there is no number at [row,col]
                        if self.board[row][col] == EMPTY != self.board[focused_row][col]:
                            self.board[row][col] = self.board[focused_row][col]
                            self.board[focused_row][col] = EMPTY
                            ever_moved = True
                        # if root = focused
                        elif self.board[row][col] == self.board[focused_row][col] != EMPTY and ever_added == False:
                            self.board[row][col] *= 2
                            self.board[focused_row][col] = EMPTY
                            ever_added = True
                            ever_moved = True
                        # if there is another number at focused
                        elif self.board[row][col] != self.board[focused_row][col] != EMPTY:
                            break
            return ever_moved
        # down
        elif direction == DOWN:
            for col in range(SIZE):
                for row in range(SIZE - 1, 0 - 1, -1):
                    ever_added = False
                    for focused_row in range(row - 1, 0 - 1, -1):
                        # if there is no number at [row, col]
                        if self.board[row][col] == EMPTY != self.board[focused_row][col]:
                            self.board[row][col] = self.board[focused_row][col]
                            self.board[focused_row][col] = EMPTY
                            ever_moved = True
                        # if root = focused
                        elif self.board[row][col] == self.board[focused_row][col] != EMPTY and ever_added == False:
                            self.board[row][col] *= 2
                            self.board[focused_row][col] = EMPTY
                            ever_moved = True
                            ever_added = True
                        # if there is another number at focused
                        elif self.board[row][col] != self.board[focused_row][col] != EMPTY:
                            break
            return ever_moved
        # left               
        elif direction == LEFT:
            for row in range(SIZE):
                for col in range(SIZE):
                    ever_added = False
                    for focused_col in range(col + 1, SIZE):
                        # if there is no number at [row,col]
                        if self.board[row][col] == EMPTY != self.board[row][focused_col]:
                            self.board[row][col] = self.board[row][focused_col]
                            self.board[row][focused_col] = EMPTY
                            ever_moved = True
                        # if root = focused
                        elif self.board[row][col] == self.board[row][focused_col] != EMPTY and ever_added == False:
                            self.board[row][col] *= 2
                            self.board[row][focused_col] = EMPTY
                            ever_moved = True
                            ever_added = True
                        # if there is another number at focused
                        elif self.board[row][col] != self.board[row][focused_col] != EMPTY:
                            break
            return ever_moved
        # right
        elif direction == RIGHT:
            for row in range(SIZE):
                for col in range(SIZE - 1, 0 - 1, -1):
                    ever_added = False
                    for focused_col in range(col - 1, 0 - 1, -1):
                        # if there is no number at [row,col]
                        if self.board[row][col] == EMPTY != self.board[row][focused_col]:
                            self.board[row][col] = self.board[row][focused_col]
                            self.board[row][focused_col] = EMPTY
                            ever_moved = True
                        # if root = focused
                        elif self.board[row][col] == self.board[row][focused_col] != EMPTY and ever_added == False:
                            self.board[row][col] *= 2
                            self.board[row][focused_col] = EMPTY
                            ever_moved = True
                            ever_added = True
                            # if there is another number at focused
                        elif self.board[row][col] != self.board[row][focused_col] != EMPTY:
                            break
            return ever_moved
        # invalid direction
        else:
            logging.critical('UNEXPECTED VALUE of DIRECTION at move')
            return ERROR
        

if __name__ == "__main__":
    for i in range(16):
        print('---------------------')
    test_board = Board()
    test_board.print()
