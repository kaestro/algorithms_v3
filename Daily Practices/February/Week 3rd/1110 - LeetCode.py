# https://leetcode.com/problems/delete-nodes-and-return-forest/description/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Delete nodes in the to_delete, and return the roots of the forests(which are the trees after deleting the nodes)
# prototype
# 1. preorder traverse the tree, and delete the nodes in the to_delete list
# 2. if the node is in the to_delete list, then add the left and right child to the result list
# *. specification: for the numbers inside to_delete needs to be read multiple times, so it's better to use set
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []
        if root.val not in to_delete_set:
            result.append(root)
        self.postorder(root, to_delete_set, result)
        return result

    def postorder(self, node: Optional[TreeNode], to_delete_set: set[int], result: List[TreeNode]):
        if node is None:
            return None

        # Postorder traversal: left, right, then node
        node.left = self.postorder(node.left, to_delete_set, result)
        node.right = self.postorder(node.right, to_delete_set, result)

        if node.val in to_delete_set:
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return None  # Delete the node

        return node  # Keep the node