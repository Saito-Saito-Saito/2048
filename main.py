#! usr/bin/env/ Python3
# main.py
# coded by Saito-Saito-Saito
# last edited: 25 September 2020
# explained on https://Saito-Saito-Saito.github.io/2048


from config import *
import board
import random


### LOG SET UP
logger = logger_setup(__name__, level=DEBUG)
logger.info('start')



parameters = {'size': DEFAULT_SIZE, 'goal': DEFAULT_GOAL}



### SET UP
def settings(command: str): # when command is X, change the parameters
    while command in ['x', 'X']:
        setcommand = input('ENTER THE COMMAND (BOARD SIZE: S,  GOAL: G,  EXIT: E) ---')
        while setcommand in ['s', 'S']:
            size_command = input('NEW SIZE --- ')
            if size_command.isdecimal() == True and int(size_command) >= 2:
                parameters['size'] = int(size_command)
                break
            else:
                print('INVALID INPUT')
                continue
        while setcommand in ['G', 'g']:
            goal_command = input('NEW GOAL (8 ~ {}) ---'.format(MAX_GOAL))
            if goal_command.isdecimal() == True:
                if 8 <= int(goal_command) < MAX_GOAL:
                    parameters['goal'] = int(goal_command)
                    break
                else:
                    print('INVALID VALUE')
                    continue
            else:
                print('INVALID INPUT')
                continue
        if setcommand in ['E', 'e']:
           return
        print('''SETTINGS
    BOARD SIZE  {} * {}
    GOAL        {}      '''.format(parameters['size'],parameters['size'],parameters['goal']))

 
def startmenu():
    command = input('''
2048

SETTINGS
    BOARD SIZE  {} * {}
    GOAL        {}
    
ENTER TO SART(X TO CHANGE THE SETTINGS) - - - '''.format(parameters['size'],parameters['size'],parameters['goal']))
    
    settings(command)



if __name__ == "__main__":
    startmenu()
    main_board = board.Board(size=parameters['size'], goal=parameters['goal'])
    main_board.print()

    while True:
        input_d = input('DIRECTION: UP-1, DOWN-2, LEFT-3, RIGHT-4 : ')
        logger.debug('input_d = {}'.format(input_d))
        if input_d in ['1', 'w', 'W']:
            direction = UP
        elif input_d in ['2', 's', 'S']:
            direction = DOWN
        elif input_d in ['3', 'a', 'A']:
            direction = LEFT
        elif input_d in ['4', 'd', 'D']:
            direction = RIGHT
        else:
            print('INVALID INPUT')
            continue
        if main_board.move(direction) == FAILED:
            print('INVALID DIRECTION')
            continue
        if main_board.insert() == FAILED or main_board.isOver():
            main_board.print()
            print('GAME OVER...')
            break
        if main_board.isGoal() == True:
            main_board.print()
            print('You WIN!')
            break
        main_board.print()
        

    logger.info('end')