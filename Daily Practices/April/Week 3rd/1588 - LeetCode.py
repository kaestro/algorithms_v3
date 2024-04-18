# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

from typing import List

class Solution:
    # array의 subarray의 길이가 홀수일 때의 합을 구하는 문제
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # Prefix sum을 이용하여 subarray의 합을 구하는 방법
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        prefix_sum = self.prefix_sum(arr)
        for subArrLength in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - subArrLength + 1):
                result += prefix_sum[i + subArrLength] - prefix_sum[i]

        return result

    def prefix_sum(self, arr):
        prefix_sum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        return prefix_sum
    
    # https://leetcode.com/problems/sum-of-all-odd-length-subarrays/solutions/854184/java-c-python-o-n-time-o-1-space/?source=submission-ac
    # O(n) time complexity, O(1) space complexity
    # arr[k] 원소가 포함된 subarray의 개수는 (k + 1) * (n - k)이다.
    # 이 중 홀수의 개수는 {(k + 1) * (n - k) + 1} // 2이다.
    # 배열의 길이가 홀/짝의 갯수는 홀수만 유일하게 길이가 홀수 일 때 1개 많을 수 있다.
    def betterSumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            result += ((i + 1) * (len(arr) - i) + 1) // 2 * arr[i]
        return result
