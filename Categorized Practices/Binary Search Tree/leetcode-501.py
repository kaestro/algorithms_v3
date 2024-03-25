# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(lst):
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while i < len(lst) and queue:
        current_node = queue.pop(0)

        if lst[i] is not None:
            current_node.left = TreeNode(lst[i])
            queue.append(current_node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            current_node.right = TreeNode(lst[i])
            queue.append(current_node.right)

        i += 1
    
    return root

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        num_cnt = defaultdict(int)

        while queue:
            current_node = queue.pop(0)
            num_cnt[current_node.val] += 1

            if current_node.left is not None:
                queue.append(current_node.left)
            
            if current_node.right is not None:
                queue.append(current_node.right)
        
        max_count = max(num_cnt.values())
        modes = [key for key, count in num_cnt.items() if count == max_count]

        return modes


if __name__ == "__main__":
    roots_list = [ [1, None, 2, 2], [0], [1, None, 2] ]
    for roots in roots_list:
        bst = list_to_tree(roots)
        print("hello")
        print(Solution().findMode(bst))