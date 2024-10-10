from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxLen = max(len(word) for word in s.split())
