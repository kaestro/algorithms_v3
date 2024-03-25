# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

from typing import List, Optional
from itertools import permutations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root: TreeNode, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    
    return root


def are_bsts_equivalent(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        return (
            root1.val == root2.val
            and are_bsts_equivalent(root1.left, root2.left)
            and are_bsts_equivalent(root1.right, root2.right)
        )
    else:
        return False


def generate_permutations(n):
    # Create a list of integers from 1 to n
    elements = list(range(1, n+1))

    # Generate all permutations
    all_permutations = list(permutations(elements))

    # Convert tuples to lists for easier manipulation if needed
    all_permutations = [list(permutation) for permutation in all_permutations]

    return all_permutations


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        any_ordered_bst = []

        all_permutations = generate_permutations(n)
        
        for permutation in all_permutations:
            bst_candidate = TreeNode(permutation[0])
            for num in permutation[1:]:
                insert(bst_candidate, num)
            
            is_available = True
            for bst in any_ordered_bst:
                if are_bsts_equivalent(bst, bst_candidate):
                    is_available = False
                    break
            
            if is_available:
                any_ordered_bst.append(bst_candidate)

        return any_ordered_bst


if __name__ == "__main__":
    Solution().generateTrees(3)