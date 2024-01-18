from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None:
            return None

        return self.constructBST(nums, 0, len(nums) - 1)
    

    def constructBST(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        root.left = self.constructBST(nums, left, mid - 1)
        root.right = self.constructBST(nums, mid + 1, right)

        return root


if __name__ == "__main__":
    list_nums = [[-10,-3,0,5,9], [1,3]]
    for idx, nums in enumerate(list_nums):
        obj = Solution()
        sample = obj.sortedArrayToBST(nums)
        print_tree(sample)