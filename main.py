from __future__ import unicode_literals
import os
import sys
import time
from constants import RUN_A, RUN_B, RUN_SAMPLE_A, RUN_SAMPLE_B
from days import day_1


#######################################################################################################################
# Main function
#######################################################################################################################
def __main__():
    # # # # # # # # # # # #
    # day_1.run(RUN_A)
    # # # # # # # # # # # #
    # day_1.run(RUN_B)
    # # # # # # # # # # # #
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