#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

# 
def sockMerchant(len_colors_list, colors_list) -> int:
    color_existence = defaultdict(int)

    num_pairs = 0

    for color in colors_list:
        if color_existence[color] == 1:
            color_existence[color] = 0
            num_pairs += 1
        else:
            color_existence[color] = 1

    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
