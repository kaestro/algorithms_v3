# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # head는 integer로 이루어진 linked list의 head node이다.
    # linked list의 연속된 node들의 합이 0이 되는 부분을 제거한 linked list를 반환하라.

    # 1. head를 순회하며 각 node의 합을 구한다.
    # 2. 합이 0이 되는 부분을 찾아서 제거한다.
    # 3. 제거된 linked list를 반환한다.

    # 분석:
    # O(n^2)의 시간복잡도를 가진다.
    # head를 순회하며 각 node의 합을 구하는데 O(n)의 시간이 걸리고,
    # 각 node의 합이 0이 되는 부분을 찾아서 제거하는데 O(n)의 시간이 걸린다.
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head가 None이면 None을 반환한다.
        if head is None:
            return None
        
        root = ListNode(0)
        # head를 순회하며 각 node의 합을 구한다.
        # O(n)의 시간복잡도를 가진다.
        previous = root
        previous.next = head
        current = head
        while current is not None:
            sum = 0
            temp = current
            while temp is not None:
                sum += temp.val
                if sum == 0:
                    previous.next = temp.next # 합이 0이 되는 부분을 제거한다.
                    break
                temp = temp.next
            else:  # This will execute if the inner loop did not break, i.e., sum != 0
                previous = previous.next
            current = previous.next
        
        return head