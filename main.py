import os
import sys
import time
from constants import RUN_A, RUN_B
from day_runner import run


#######################################################################################################################
# Main function
#######################################################################################################################
def __main__():
    # # # # # # # # # #
    # run(1, RUN_A)
    # # # # # # # # # #
    # run(1, RUN_B)
    # # # # # # # # # #
    # run(2, RUN_A)
    # # # # # # # # # #
    # run(2, RUN_B)
    # # # # # # # # # #
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