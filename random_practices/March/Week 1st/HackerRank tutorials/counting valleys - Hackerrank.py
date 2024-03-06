# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(num_steps, steps_list) -> int:

    sea_level = 0
    num_valleys = 0

    for step in steps_list:
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                num_valleys += 1
        else:
            sea_level -= 1
    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
