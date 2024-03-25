from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node: Node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        insert(node.left, key)
    elif key > node.right:
        insert(node.right, key)
    
    return node


def inorder(root: Node):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def preorder_copy(original_node: Node):
    if original_node is None:
        return None

    new_node = Node(original_node.key)

    new_node.left = preorder_copy(original_node.left)
    new_node.right = preorder_copy(original_node.right)
    
    return new_node


def level_order_traversal(root: Node):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.key)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)