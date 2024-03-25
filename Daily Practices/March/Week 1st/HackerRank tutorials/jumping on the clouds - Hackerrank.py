# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

# you can jump 1 or 2 steps
# 0 is safe, 1 is not safe
# find the minimum number of jumps to reach the end
def jumpingOnClouds(clouds_list: List[int]):

    min_jumps = [0] * len(clouds_list)

    if clouds_list[1] == 0:
        min_jumps[1] = 1
    if len(clouds_list) > 2:
        if clouds_list[2] == 0:
            min_jumps[2] = 1
        else:
            min_jumps[2] = float('inf')

    for i in range(3, len(clouds_list)):
        if clouds_list[i] == 0:
            min_jumps[i] = 1 + min(min_jumps[i-1], min_jumps[i-2])
        else:
            min_jumps[i] = float('inf')

    return min_jumps[-1]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    '''
    fptr.write(str(result) + '\n')

    fptr.close()
    '''
