# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        queue = deque([(root.left, root.right)])

        while queue:
            node1, node2 = queue.popleft()

            if node1 is None and node2 is None:
                continue
            elif None in [node1, node2]:
                return False
            elif node1.val != node2.val:
                return False
            
            # Key idea to check for symmetry
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))

        return True