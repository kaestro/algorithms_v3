# https://leetcode.com/problems/binary-watch/
from typing import List

class Solution:
    # LED가 켜진 개수가 주어졌을 때, 가능한 모든 시간을 반환하는 문제
    # LED는 2진법으로 이루어진 수를 나타내고, 4개의 LED가 시간을 나타내고, 6개의 LED가 분을 나타낸다.
    # hour를 나타내는 LED는 8, 4, 2, 1이 있고 이를 통해 총 0 ~ 11까지의 시간을 나타낼 수 있다.
    # minute를 나타내는 LED는 32, 16, 8, 4, 2, 1이 있고 이를 통해 총 0 ~ 59까지의 분을 나타낼 수 있다.
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        def backTrack(turnedOn, start, hour, minute, result):
            if turnedOn == 0:
                if hour < 12 and minute < 60:
                    result.append(f"{hour}:{minute:02d}")
                return

            for i in range(start, 10):
                if i < 4:
                    backTrack(turnedOn - 1, i + 1, hour + (1 << i), minute, result)
                else:
                    backTrack(turnedOn - 1, i + 1, hour, minute + (1 << (i - 4)), result)

        result = []
        backTrack(turnedOn, 0, 0, 0, result)

        return result