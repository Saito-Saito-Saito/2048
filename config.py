#! usr/bin/env/ Python3
# config.py
# coded by Saito-Saito-Saito
# last edited: 28 June 2020



from logging import getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO, WARNING, ERROR, CRITICAL



### LOG SET UP
DEFAULT_LOG_FILE_NAME = 'log.txt'
DEFAULT_LOG_FORMAT = Formatter('%(asctime)s - %(levelname)s -　logger:%(name)s - %(filename)s - L%(lineno)d - %(funcName)s - %(message)s')

# file handler
DEFAULT_FHANDLER = FileHandler(DEFAULT_LOG_FILE_NAME, mode='w')
DEFAULT_FHANDLER.setFormatter(DEFAULT_LOG_FORMAT)
DEFAULT_FHANDLER.setLevel(DEBUG)
# stream handler
DEFAULT_SHANDLER = StreamHandler()
DEFAULT_SHANDLER.setFormatter(DEFAULT_LOG_FORMAT)
DEFAULT_SHANDLER.setLevel(WARNING)

# set up function
def logger_setup(logger_name='default', level=DEBUG, *, fhandler=None, fhandler_level=DEBUG, filename=DEFAULT_LOG_FILE_NAME, filemode='w', fileformat=DEFAULT_LOG_FORMAT, shandler=None, shandler_level=WARNING, streamformat=DEFAULT_LOG_FORMAT):
    logger = getLogger(logger_name)
    logger.setLevel(level)
    
    # file handler
    fhandler = fhandler or FileHandler(filename, mode=filemode)
    fhandler.setLevel(fhandler_level)
    fhandler.setFormatter(fileformat)
    logger.addHandler(fhandler)
    
    # stream handler
    shandler = shandler or StreamHandler()
    shandler.setLevel(shandler_level)
    shandler.setFormatter(streamformat)
    logger.addHandler(shandler)
    
    return logger



### INDEXES
ROW = 0
COL = 1



### SQUARES STATUS
EMPTY = 0



### DIRECTIONS
UP = [-1, 0]
DOWN = [+1, 0]
LEFT = [0, -1]
RIGHT = [0, +1]



### RETURN VALUES
SUCCEEDED = True
FAILED = False



### DEFAULT VALUES
DEFAULT_PROB4 = 1 / 8
DEFAULT_SIZE = 4  # board size = 4 * 4
DEFAULT_GOAL = 2048
MAX_GOAL = 65536



