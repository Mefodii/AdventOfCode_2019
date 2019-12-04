import os
import sys
import time
from constants import PART_TWO, PART_ONE
from day_runner import run


#######################################################################################################################
# Main function
#######################################################################################################################
def __main__():
    ###################
    # run(1, PART_ONE)
    ###################
    # run(1, PART_TWO)
    ###################
    # run(2, PART_ONE)
    ###################
    # run(2, PART_TWO)
    ###################
    # run(3, PART_ONE, True)
    ###################
    # run(3, PART_TWO, True)
    ###################
    # run(3, PART_ONE)
    ###################
    # run(3, PART_TWO)
    ###################
    # run(4, PART_ONE, True)
    # ###################
    # run(4, PART_ONE)
    ###################
    run(4, PART_TWO)
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