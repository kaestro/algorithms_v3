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
        
        return root.next
    
    # 분석:
    # O(n)의 시간복잡도를 가진다.
    # head를 순회하며 각 node의 합을 구하는데 O(n)의 시간이 걸리고,
    # 각 node의 합이 0이 되는 부분을 찾아서 제거하는데 O(1)의 시간이 걸린다.

    # head에서 순회하면서 accumulated sum을 구한다.
    # 그런데 만일 head 이후의 node(current)에서 출발해 accumulated sum이 같은 값이 나오면,
    # 그 노드들 사이의 합은 0이 된다.
    # 그러므로, current node를 해당 accumulated sum의 node의 다음으로 바꿔주면 된다.
    # 문제는, 이 때 current node 이전의 node로 연결되면 안된다는 것인데 이런 경우는 존재할 수 없다.
    # 왜냐하면 현재 sum_to_node에 있는 node는 해당 list 상에서 해당 값을 가지는 가장 마지막 node이기 때문이다.
    def advancedRemoveZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        accumulated_sum = 0
        sum_to_node = {0: root}

        while head:
            accumulated_sum += head.val
            sum_to_node[accumulated_sum] = head
            head = head.next

        head = root
        accumulated_sum = 0
        while head:
            accumulated_sum += head.val
            # 만일 accumulated_sum이 sum_to_node에 있다면, 그 노드들 사이의 합은 0이 된다.
            # 때문에, head와 sum_to_node[accumulated_sum] 사이의 노드들을 제거한다.
            if accumulated_sum in sum_to_node:
                head.next = sum_to_node[accumulated_sum].next
            head = head.next

        return root.next