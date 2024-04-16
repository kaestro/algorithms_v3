# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/

from typing import List

class Solution:
    # two rules must be satisfied after the operation:
    # 1. The first element must be 1
    # 2. The difference between the current element and the previous element must be less than or equal to 1

    # two operations can be done on each element:
    # decrease the element to any number less than or equal to the current element
    # rearrange the elements in any order

    # Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

    # => It means that it is much more preferred to rearrange the elements compared to decreasing the elements.

    # ideal case: each elements' difference is 1 when sorted in ascending order

    # Then the problem is, the gaps between the elements are not 1, which can't be removed by rearranging the elements.

    # We also need to consider that the elements can be either increased or decreased.
    # => 연속한 숫자들이 짝수개의 pair로 만들어지면 gap이 생기고, 홀수개의 pair로 만들어지면 1개씩 있는것과 동일하다.
    # => 단독으로 있는 경우만 따로 처리해주면 된다. => 얘를 이용해서 gap을 채워주자.
    
    # => gap이 있을 때는 그거 위에서 중복된 것으로 메꿔주고, 남는 것들에 대해서 생각하면 됨?
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        result = 0

        # step 1: sort the array
        arr.sort()

        # step 2: gap을 찾는다.
        soreted_set_arr = sorted(list(set(arr)))
        self.findGap(soreted_set_arr)

        # step 3: gap을 메꾼다.

        # step 4: 남은 수의 갯수가 정답이다.

        return result
    
    # distinct sorted array여야 한다
    def findGap(self, arr: List[int]) -> List[set[int]]:
        curr_num = 1
        max_num = arr[-1]
        result = []
        curr_gap = (-1, -1)
        idx_list = 0

        while curr_num < max_num:
            if curr_num == arr[idx_list]:
                idx_list += 1
                curr_num += 1
                continue
            
            if curr_gap[0] == -1:
                curr_gap = (idx_list, -1)
            else:
                while curr_num != arr[idx_list]:
                    idx_list += 1
                    curr_num += 1
            
            idx_list += 1
            curr_num += 1
        
        return result


if __name__ == "__main__":
    sample = Solution()
    print(sample.maximumElementAfterDecrementingAndRearranging([100,1,1000])) # 2