# https://leetcode.com/problems/beautiful-arrangement/description/

from itertools import permutations

class Solution:
    # num_integers가 들어왔을 때 가능한 모든 순열을 구하고, 그 중에서 조건을 만족하는 순열의 개수를 반환하는 문제
    # 조건 1) permutation[i] % i == 0
    # 조건 2) i % permutation[i] == 0

    # Brute Force
    # 1. permutation을 구한다.
    # 2. 조건을 만족하는 순열의 개수를 센다.
    # Time Complexity: O(n!) => permutation을 구하는데 O(n!)이 걸린다.

    # => permutation을 안 구하고 조건을 만족하는 순열의 개수를 세는 방법은 없을까?

    # Solution 1)
    # 각각의 index 타고 내려가면서 나눌 수 있는 숫자들만을 이용해서 loop 돌리고, 사용 여부를 저장한다.
    # Problem => 순열을 구하는 것과 같은 문제가 된다. O(n!)이 걸린다.

    # Solution 2)
    # Backtracking을 이용해서 조건을 만족하는 순열을 구한다.
    # Time Complexity: O(k) => k는 조건을 만족하는 순열의 개수

    # Solution 3)
    # 둘을 합쳐서, 매번 index를 나눌 수 있는지 연산하지 않고 미리 나눌 수 있는 숫자들을 저장해둔 뒤
    # backtracking을 한다.
    def countArrangement(self, num_integers: int) -> int:
        def is_beautiful(arrangement):
            for i, num in enumerate(arrangement):
                if num % (i + 1) != 0 and (i + 1) % num != 0:
                    return False
            return True

        beautiful_count = 0

        for permutation in permutations(range(1, num_integers + 1)):
            if is_beautiful(permutation):
                beautiful_count += 1

        return beautiful_count
    
    # solution 2 implementation
    def backTrackCountArrangement(self, num_integers: int) -> int:
        def backTrack(index, arrangement, used):
            if index == 0:
                beautiful_count[0] += 1
                return
            
            for i in range(1, num_integers + 1):
                if not used[i] and (i % index == 0 or index % i == 0):
                    used[i] = True
                    backTrack(index - 1, arrangement, used)
                    used[i] = False

        used = [False] * (num_integers + 1)
        beautiful_count = [0]

        backTrack(num_integers, list(range(1, num_integers + 1)), used)

        return beautiful_count[0]
    
    # solution 3 implementation
    def backTrackCountArrangementWithPruning(self, num_integers: int) -> int:
        def backTrack(index, arrangement, used):
            if index == 0:
                beautiful_count[0] += 1
                return
            
            for num in is_beautiful[index]:
                if not used[num]:
                    used[num] = True
                    backTrack(index - 1, arrangement, used)
                    used[num] = False

        used = [False] * (num_integers + 1)
        beautiful_count = [0]
        is_beautiful = [[] for _ in range(num_integers + 1)]

        for index in range(1, num_integers + 1):
            for num in range(1, num_integers + 1):
                if index % num == 0 or num % index == 0:
                    is_beautiful[index].append(num)

        backTrack(num_integers, list(range(1, num_integers + 1)), used)

        return beautiful_count[0]        