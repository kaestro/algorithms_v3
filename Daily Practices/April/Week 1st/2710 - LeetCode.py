# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        list_num = list(num)
        while list_num and list_num[-1] == '0':
            list_num.pop()
        return ''.join(list_num)
    
    def variousSolution1(self, num: str) -> str:
        return num.rstrip('0')
    
    def variousSolution2(self, num: str) -> str:
        num = num[::-1]
        num = int(num)
        num = str(num)
        num = num[::-1]
        return num