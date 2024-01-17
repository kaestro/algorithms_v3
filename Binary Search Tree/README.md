# <span style="color:red;"> BINARY SEARCH TREE(BST)</span>

## <span style="color:blue;"> Properties

* Each Node has at most 2 child nodes
* keys[node] where node in left_subtree < keys[root]
* keys[node] where node in right_subtree < keys[root]
* IsNodeBinaryTree(Nodes[idx]) where idx in (left_subtree || right_subtree) == True

## Traversals

* inorder Traversal
  * left -> root -> right
  * traverse nodes in non-decreasing order
* preorder Traversal
  * root -> left -> right
  * used in
    * prefix expression
    * copy the tree
* postorder Traversal
  * left -> right -> root
  * visiting subtrees of a node is ensured
  * used in
    * deleting tree
* levelorder Traversal
  * BFS
  * use queue