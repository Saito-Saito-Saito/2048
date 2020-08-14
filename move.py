#! usr/bin/env/ Python3
# move.py
# coded by Saito-Saito-Saito
# last edited: 15 August 2020
# CAUTION: THIS CODE IS ONLY FOR MEMORANDOM OF move METHOD. YOU CAN RUN main.py WITHOUT THIS MODULE.


import board
from config import *


class Move(board.Board):
    def board_move(self, direction: list, *, logger=None):
        logger = logger or self.logger
        ever_moved = False
        
        # up
        if direction == UP:
            logger.debug('direction is UP')
            root = [0, 0]
            for root[COL] in range(self.size):
                for root[ROW] in range(self.size):
                    focused = [root[ROW] + 1, root[COL]]
                    while self.isInBoard(focused[ROW]):
                        # in case root == EMPTY      
                        if self.board[root[ROW]][root[COL]] == EMPTY != self.board[focused[ROW]][focused[COL]]:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] = self.board[focused[ROW]][focused[COL]]
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                        # in case board[root]==board[focused] (!= 0)
                        elif self.board[root[ROW]][root[COL]] == self.board[focused[ROW]][focused[COL]] != 0:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] *= 2
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                            break
                        elif self.board[focused[ROW]][focused[COL]] != EMPTY:
                            break
                        focused[ROW] += 1
        elif direction == DOWN:
            logger.debug('direction is DOWN')
            root = [0, 0]
            for root[COL] in range(self.size):
                for root[ROW] in range(self.size - 1, -1, -1):
                    focused = [root[ROW] - 1, root[COL]]
                    while self.isInBoard(focused[ROW]):
                        # in case root == EMPTY      
                        if self.board[root[ROW]][root[COL]] == EMPTY != self.board[focused[ROW]][focused[COL]]:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] = self.board[focused[ROW]][focused[COL]]
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                        # in case board[root]==board[focused] (!= 0)
                        elif self.board[root[ROW]][root[COL]] == self.board[focused[ROW]][focused[COL]] != 0:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] *= 2
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                            break
                        elif self.board[focused[ROW]][focused[COL]] != EMPTY:
                            break
                        focused[ROW] -= 1
        elif direction == LEFT:
            logger.debug('direction is LEFT')
            root = [0, 0]
            for root[ROW] in range(self.size):
                for root[COL] in range(self.size):
                    focused = [root[ROW], root[COL]+1]
                    while self.isInBoard(focused[COL]):
                        # in case root == EMPTY      
                        if self.board[root[ROW]][root[COL]] == EMPTY != self.board[focused[ROW]][focused[COL]]:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] = self.board[focused[ROW]][focused[COL]]
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                        # in case board[root]==board[focused] (!= 0)
                        elif self.board[root[ROW]][root[COL]] == self.board[focused[ROW]][focused[COL]] != 0:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] *= 2
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                            break
                        elif self.board[focused[ROW]][focused[COL]] != EMPTY:
                            break
                        focused[COL] += 1
        elif direction == RIGHT:
            logger.debug('direction is RIGHT')
            root = [0, 0]
            for root[ROW] in range(self.size):
                for root[COL] in range(self.size - 1, -1, -1):
                    focused = [root[ROW], root[COL] - 1]
                    while self.isInBoard(focused[COL]):
                        # in case root == EMPTY      
                        if self.board[root[ROW]][root[COL]] == EMPTY != self.board[focused[ROW]][focused[COL]]:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] = self.board[focused[ROW]][focused[COL]]
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                        # in case board[root]==board[focused] (!= 0)
                        elif self.board[root[ROW]][root[COL]] == self.board[focused[ROW]][focused[COL]] != 0:
                            logger.info('{}, {} <- {}'.format(root[ROW], root[COL], self.board[focused[ROW]][focused[COL]]))
                            self.board[root[ROW]][root[COL]] *= 2
                            self.board[focused[ROW]][focused[COL]] = EMPTY
                            ever_moved = True
                            break
                        elif self.board[focused[ROW]][focused[COL]] != EMPTY:
                            break
                        focused[COL] -= 1
        else:
            logger.error('INPUT DIRECTION is INVALID VALUE')
            return FAILED

        if ever_moved == True:
            return SUCCEEDED
        else:
            # if no number was moved, it is game over
            logger.debug('ever_moved == False')
            return FAILED


if __name__ == "__main__":
    test_board = Move()
    test_board.print()

    test_board.board_move(UP)
    test_board.insert()
    test_board.print()
    test_board.board_move(DOWN)
    test_board.insert()
    test_board.print()
    test_board.board_move(LEFT)
    test_board.insert()
    test_board.print()
    test_board.board_move(RIGHT)
    test_board.insert()
    test_board.print()
