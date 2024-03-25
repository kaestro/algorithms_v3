from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return 0
        stack=[root]
        dic={}
        while stack:
            node=stack.pop()
            if node:
                if node.val in dic:
                    return 1
                else:
                    dic[k-node.val]=1
                stack.append(node.left)
                stack.append(node.right)
        return 0