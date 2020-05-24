#! usr/bin/env python3
# play.py
# coded by Saito-Saito-Saito

from config import *
import board

def playmode():
    playboard = board.Board()
    playboard.print()

    while True:
        # if already cleared
        status = playboard.setcheck()
        if status == GAME_CLR:
            print('GAME CLEAR!!')
            break
        elif status == GAME_OVR:
            print('NO WAY TO MOVE')
            print('GAME OVER ...')
            break
        
        # direction
        input_direc = input('Enter the direction (1:up  2:down  3:left  4:right)  --- ')
        try:
            direction = int(input_direc)
        except:
            print('INVALID INPUT')
            continue
        if direction not in [UP, DOWN, LEFT, RIGHT]:
            print('INVALID INPUT')
            continue

        if playboard.move(direction) == SUCCEEDED:
            playboard.appear()
            playboard.print()
        


if __name__ == "__main__":
    playmode()