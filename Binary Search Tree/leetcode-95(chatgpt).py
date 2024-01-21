class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_trees(n):
    if n == 0:
        return []
    return generate_trees_helper(1, n)

def generate_trees_helper(start, end):
    result = []
    
    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_trees = generate_trees_helper(start, i - 1)
        right_trees = generate_trees_helper(i + 1, end)

        for left_tree in left_trees:
            for right_tree in right_trees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)

    return result