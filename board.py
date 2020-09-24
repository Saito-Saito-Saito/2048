#! usr/bin/env/ Python3
# board.py
# coded by Saito-Saito-Saito
# last edited: 25 September 2020
# explained on https://Saito-Saito-Saito.github.io/2048


from config import *
import copy
import random


local_logger = logger_setup(__name__, level=INFO)



class Board:
    def insert(self, *, logger=None):
        logger = logger or self.logger

        # searching for empty square
        emptied = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == EMPTY:
                    emptied.append([row, col])

        # when there is no empty square, you cannot insert a number
        if emptied == []:
            logger.info('there is no empty square')
            return FAILED

        # selecting an empty square randomly
        target = random.choice(emptied)

        # inserting 4 if random No < prob4
        if random.random() < self.prob4:
            self.board[target[ROW]][target[COL]] = 4
        else:
            self.board[target[ROW]][target[COL]] = 2

        logger.info('target {} <- No. {}'.format(target, self.board[target[ROW]][target[COL]]))
        return SUCCEEDED


    def __init__(self, *, size=DEFAULT_SIZE, board=[], goal=DEFAULT_GOAL, logger=local_logger, prob4=DEFAULT_PROB4):
        # copying the parameters
        self.size = size
        self.prob4 = prob4
        self.logger = logger
        if goal > MAX_GOAL:
            self.goal = MAX_GOAL
        else:
            self.goal = goal

        # copying the board
        if len(board) == self.size:
            self.board = copy.deepcopy(board)
        else:
            self.board = [[EMPTY for col in range(self.size)] for row in range(self.size)]
            self.insert(logger=logger)
            self.insert(logger=logger)

        logger.debug('in {}, board is {}'.format(self, self.board))


    # checking whether index is in the board 
    def isInBoard(self, index:int):
        if 0 <= index < self.size:
            return True
        else:
            return False


    def print(self):
        print('\n-', end='')
        for row in range(self.size):
            print('--------', end='')
        print('')   # to a new line
        for row in range(self.size):
            print('|', end='')
            for col in range(self.size):
                if self.board[row][col] == EMPTY:
                    print('       |', end='')
                else:
                    print(' {} '.format(self.board[row][col]).center(7) + '|', end='')
            print('\n-', end='')  # to new line
            for col in range(self.size):
                print('--------', end='')
            print('')  # to a new line
        print('')   # to a new line
        return SUCCEEDED


    def move(self, direction: list, *, logger=None):
        logger = logger or self.logger
        ever_moved = False
        start = [0, self.size - 1]  # UP&LEFT: 0,  DOWN&RIGHT: size - 1
        step = [1, -1]  # UP&LEFT: 1,  DOWN&RIGHT: -1
        stop = [self.size, -1]  # UP&LEFT: size,  DOWN&RIGHT: -1
        switch = (direction in [DOWN, RIGHT])   # UP&LEFT: False,  DOWN&RIGHT: True
        
        # cf. move.py and https://Saito-Saito-Saito.github.io/2048/stage4
        root = [0, 0]
        for root[COL] in range(start[switch], stop[switch], step[switch]):
            for root[ROW] in range(start[switch], stop[switch], step[switch]):
                focused = [root[ROW] - direction[ROW], root[COL] - direction[COL]]
                while self.isInBoard(focused[ROW]) and self.isInBoard(focused[COL]):
                    # in case root == EMPTY
                    if self.board[root[ROW]][root[COL]] == EMPTY != self.board[focused[ROW]][focused[COL]]:
                        logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                        self.board[root[ROW]][root[COL]] = self.board[focused[ROW]][focused[COL]]
                        self.board[focused[ROW]][focused[COL]] = EMPTY
                        ever_moved = True
                    # in case root == focused != EMPTY
                    elif self.board[root[ROW]][root[COL]] == self.board[focused[ROW]][focused[COL]] != EMPTY:
                        logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                        self.board[root[ROW]][root[COL]] *= 2
                        self.board[focused[ROW]][focused[COL]] = EMPTY
                        ever_moved = True
                        break
                    # in case EMPTY != root != focuseed != EMPTY
                    elif self.board[focused[ROW]][focused[COL]] != EMPTY:
                        break
                    # either is zero
                    focused[ROW] -= direction[ROW]
                    focused[COL] -= direction[COL]

        if ever_moved == True:
            return SUCCEEDED
        else:
            # if no number was moved, it is game over
            logger.debug('ever_moved == False')
            return FAILED


    def isGoal(self, *, logger=None):
        logger = logger or self.logger
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] >= self.goal:
                    logger.info('{} is goaled'.format([row, col]))
                    return True
        # there is no goaled square
        return False


    def isOver(self, *, logger=None):
        logger = logger or self.logger
        local_board = Board(size=self.size, board=self.board, goal=self.goal, logger=self.logger, prob4=self.prob4)
        for direction in [UP, DOWN, LEFT, RIGHT]:
            if local_board.move(direction):
                logger.info('direction {} is available'.format(direction))
                return False
        # here, no move is available
        return True



if __name__ == "__main__":    
    test_board = Board(logger=local_logger)
    test_board.print()
    # for count in range(16):
    #     test_board.move(random.choice([UP, DOWN, LEFT, RIGHT]))
    #     test_board.print()
    test_board.move(random.choice([UP, DOWN, LEFT, RIGHT]))
    test_board.insert()
    test_board.print()