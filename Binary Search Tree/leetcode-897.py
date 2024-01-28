# https://leetcode.com/problems/increasing-order-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=1, left=None, right=None):
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
    def increasingBST(self, root: TreeNode) -> TreeNode:

        if root is None:
            return None

        def inorder_traversal(node):
            if node is None:
                return []
            
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_values = inorder_traversal(root)
        new_root = current_node = TreeNode(sorted_values[0])

        for val in sorted_values[1:]:
            current_node.right = TreeNode(val)
            current_node = current_node.right

        return new_root
    

    # 따로 리스트에다가 저장한 뒤 트리를 만들지 않고, 바로 트리를 편다.
    def exemplary_increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        def inorder_traversal(node):
            if node is None:
                return
            
            inorder_traversal(node.left)
            self.current_node.right = TreeNode(node.val)
            self.current_node = self.current_node.right
            inorder_traversal(node.right)
        
        new_root = self.current_node = TreeNode()
        inorder_traversal(root)
        return new_root.right


if __name__ == "__main__":
    TreeLists = [ [5,3,6,2,4,None,8,1,None,None,None,7,9], [5,1,7] ]
    for treeList in TreeLists:
        BST = list_to_tree(treeList)
        orderedList = Solution().increasingBST(BST)
        print("hello")
