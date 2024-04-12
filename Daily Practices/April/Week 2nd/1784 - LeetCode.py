# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s_list = list(s)

        prev = s_list.pop()
        count = 1 if prev == "1" else 0
        while s_list:
            curr = s_list.pop()
            if prev != curr:
                prev = curr
                if curr == "1":
                    count += 1
                    if count > 1:
                        return False
        
        return True
                

