# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr: List[List[int]]):
    max_hourglass_sum = float('-inf')

    for row_index in range(4):
        for col_index in range(4):
            top = sum(arr[row_index][col_index:col_index+3])
            middle = arr[row_index+1][col_index+1]
            bottom = sum(arr[row_index+2][col_index:col_index+3])
            hourglass_sum = top + middle + bottom
            max_hourglass_sum = max(hourglass_sum, max_hourglass_sum)

    return max_hourglass_sum if max_hourglass_sum != float('-inf') else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
