# https://leetcode.com/problems/design-an-ordered-stream/description/

from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.idx = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value

        result = []
        for i in range(self.idx, len(self.stream)):
            if self.stream[i] is None:
                break
            result.append(self.stream[i])
            self.idx += 1
        
        """
        begin = self.idx
        while self.stream[self.idx]:
            self.idx += 1
        
        return self.stream[begin:self.idx]
        """

        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)