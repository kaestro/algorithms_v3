# https://leetcode.com/explore/learn/card/sorting/694/comparison-based-sorts/4485/
# Implementation of insertion sort
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self, values):
        self.head = None
        self.build_linked_list(values)
    
    def build_linked_list(self, values):
        if not values:
            return
        
        self.head = ListNode(values[0])
        current = self.head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
    
    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        print(result)


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        sorted_tail = head
        current = head.next

        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            if prev.next == current:
                sorted_tail = current
            else:
                sorted_tail.next = current.next
                current.next = prev.next
                prev.next = current
            
            current = sorted_tail.next
        
        return dummy.next

if __name__ == "__main__":
    sampleHead = SinglyLinkedList([4,2,1,3])
    sampleHead.display()

    sortedHead = Solution().insertionSortList(sampleHead.head)
    while sortedHead:
        print(sortedHead.val)
        sortedHead = sortedHead.next