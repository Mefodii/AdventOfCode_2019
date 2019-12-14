import os
import sys
import time
from constants import PART_TWO, PART_ONE
from day_runner import run


#######################################################################################################################
# Main function
#######################################################################################################################
def __main__():
    day = 14
    ###################
    # run(day, PART_ONE, True)
    ###################
    # run(day, PART_TWO, True)
    # ###################
    # run(day, PART_ONE)
    ###################
    run(day, PART_TWO)
    ###################
    pass


#######################################################################################################################
# Process
#######################################################################################################################
if __name__ == "__main__":
    # Start time of the program
    start = time.time()

    # Main functionality
    __main__()

    # End time of the program
    end = time.time()
    # Running time of the program
    print("Program ran for: ", end - start, "seconds.")