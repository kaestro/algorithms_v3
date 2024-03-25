from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def max_heapify(nums, heap_size, root):
            largest = root
            left_child = 2 * root + 1
            right_child = 2 * root + 2

            if left_child < heap_size and nums[left_child] > nums[largest]:
                largest = left_child
            
            if right_child < heap_size and nums[right_child] > nums[largest]:
                largest = right_child
            
            if largest != root:
                nums[largest], nums[root] = nums[root], nums[largest]
                max_heapify(nums, heap_size, largest)
            
        
        def build_max_heap(nums):
            for i in range(len(nums)//2 - 1, -1, -1):
                max_heapify(nums, len(nums), i)


        def heapsort(nums):
            build_max_heap(nums)
            for i in range(len(nums)-1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                max_heapify(nums, i, 0)
        
        heapsort(nums)
        return nums