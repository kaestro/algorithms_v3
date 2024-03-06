# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(input_string: str, num_repeats: int) -> int:
    num_a_in_string = input_string.count('a')
    num_a_in_remainder = input_string[:num_repeats % len(input_string)].count('a')

    total_a = (num_a_in_string * (num_repeats // len(input_string))) + num_a_in_remainder

    return total_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
