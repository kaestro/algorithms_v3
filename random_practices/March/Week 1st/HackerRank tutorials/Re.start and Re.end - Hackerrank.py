# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re

if __name__ == '__main__':
    input_string = input()
    substring = input()

    i = 0
    while i < len(input_string):
        match = re.search(substring, input_string[i:])
        if match:
            print((i + match.start(), i + match.end() - 1))
            i = i + match.start() + 1
        else:
            break

    if not re.search(substring, input_string):
        print((-1, -1))
