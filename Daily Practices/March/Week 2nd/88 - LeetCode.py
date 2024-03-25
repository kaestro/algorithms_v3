# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        left_idx, right_idx, insert_idx = 0, 0, m

        while left_idx < m and right_idx < n and insert_idx < m + n:
            if nums1[left_idx] < nums2[right_idx]:
                nums1[insert_idx] = nums1[left_idx]
                nums1[left_idx] = 0
                left_idx += 1
                insert_idx += 1
            else:
                nums1[insert_idx] = nums2[right_idx]
                right_idx += 1
                insert_idx += 1
        
        if insert_idx == m + n:
            insert_idx = 0
        else:
            while insert_idx < m + n:
                if left_idx < m:
                    nums1[insert_idx] = nums1[left_idx]
                    left_idx += 1
                    insert_idx += 1
                else:
                    nums1[insert_idx] = nums2[right_idx]
                    right_idx += 1
                    insert_idx += 1
            insert_idx = 0
        
        while left_idx < m and right_idx < n:
            if nums1[left_idx] < nums2[right_idx]:
                nums1[insert_idx] = nums1[left_idx]
                left_idx += 1
                insert_idx += 1
            else:
                nums1[insert_idx] = nums2[right_idx]
                right_idx += 1
                insert_idx += 1
        
        while left_idx < m // 2:
            nums1[insert_idx] = nums1[left_idx]
            left_idx += 1
            insert_idx += 1
        
        while right_idx < n:
            nums1[insert_idx] = nums2[right_idx]
            right_idx += 1
            insert_idx += 1
        
        nums1[m:m+n], nums1[:m] = nums1[:m], nums1[m:m+n]
    
    def improvedSolution(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        if n > 0:
            nums1[:n] = nums2[:n]