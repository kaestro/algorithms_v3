# https://leetcode.com/problems/binary-tree-paths/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Given the root of a binary tree, return all root-to-leaf paths in any order.
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def backTrack(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                paths.append("->".join(path))
            else:
                backTrack(node.left, path)
                backTrack(node.right, path)

            path.pop()
        
        backTrack(root, [])

        return paths