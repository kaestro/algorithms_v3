# https://leetcode.com/problems/all-possible-full-binary-trees/

from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # If n is even, it's not possible to create a full binary tree
        if n % 2 == 0:
            return []
        
        # Memoization to avoid recomputing the same trees
        memo = {}

        # Helper function to generate all possible full binary trees with m nodes
        def generate_trees(m):
            if m in memo:
                return memo[m]
            
            if m == 0:
                return [None]

            if m == 1:
                return [TreeNode(0)]
            
            result = []
            # Iterate through all possible left subtree sizes
            for i in range(1, m, 2):
                left_subtrees = generate_trees(i)
                right_subtrees = generate_trees(m - 1 - i)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[m] = result
            return result

        return generate_trees(n)