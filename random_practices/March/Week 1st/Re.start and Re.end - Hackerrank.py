# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re

# 모든 substring의 시작과 끝을 찾아내는 문제이다.
# finditer는 전체 중에 해당하는 모든 substring을 찾아내지 못하기 때문에
# findall을 사용해야 한다.
if __name__ == '__main__':
    input_string = input()
    substring = input()

    i = 0
    while i < len(input_string):
        match = re.search(substring, input_string[i:])
        if match:
            print((i + match.start(), i + match.end() - 1))
            i = i + match.start() + 1
        break

    if not re.search(substring, input_string):
        print((-1, -1))
