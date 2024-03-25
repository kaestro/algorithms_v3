# https://leetcode.com/problems/add-two-numbers-ii/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two integers are represented in reverse order in the linked list.
    # The most significant digit comes first.
    # Add two numbers and return the sum as a linked list.

    # Input: list_left = [7, 2, 4, 3], list_right = [5, 6, 4]
    # Output: [7, 8, 0, 7]
    # problem is, that the input is reversed.
    # Therefore, we need to reverse the input first.
    # Then, we can add the two numbers and return the sum as a linked list.
    def addTwoNumbers(self, list_left: ListNode, list_right: ListNode) -> ListNode:
        list_left = self.reverseLinkedList(list_left)
        list_right = self.reverseLinkedList(list_right)

        result = None
        carry = 0
        while list_left or list_right or carry:
            if list_left:
                carry += list_left.val
                list_left = list_left.next
            if list_right:
                carry += list_right.val
                list_right = list_right.next

            result, carry = ListNode(carry % 10, result), carry // 10

        return self.reverseLinkedList(result)

    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev