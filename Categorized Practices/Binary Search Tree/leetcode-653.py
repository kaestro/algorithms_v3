# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

from typing import Optional, List

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
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:

        if root is None:
            return False

        def bstToSortedList(node):
            result = []
            stack = []
            current = node

            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left
            
                current = stack.pop()
                result.append(current.val)

                current = current.right

            return result

        sorted_values = bstToSortedList(root)

        left_idx = 0
        right_idx = len(sorted_values) - 1
        ans = False

        while left_idx < right_idx:
            check_sum = sorted_values[left_idx] + sorted_values[right_idx]
            if check_sum < target:
                left_idx += 1
            elif check_sum > target:
                right_idx -= 1
            else:
                ans = True
                break

        return ans
    



if __name__ == "__main__":
    list_roots = [ [5,3,6,2,4,None,7], [5,3,6,2,4,None,7]]
    list_target = [9, 28]

    for i in range(len(list_roots)):
        bst = list_to_tree(list_roots[i])
        ans = Solution().findTarget(bst, list_target[i])
        if ans:
            print(str(i + 1) + "th has two sum")
        else:
            print(str(i + 1) + "th doesn't have two sum")