# https://leetcode.com/problems/path-sum/description/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        
        queue = deque([(root, 0)])

        while queue:
            node, pathSum = queue.popleft()
            pathSum += node.val

            if node.left is None and node.right is None and pathSum == targetSum:
                return True
            
            if node.left:
                queue.append((node.left, pathSum))
            if node.right:
                queue.append((node.right, pathSum))

        return False