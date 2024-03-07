# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List
from collections import Counter

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine: List[str], note: List[str]):
    magazine_words = Counter(magazine)
    note_words = Counter(note)

    for word, count in note_words.items():
        if magazine_words[word] < count:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
