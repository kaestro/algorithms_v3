# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 이진 트리의 루트와 거리가 주어졌을 때, 다음 조건을 만족하는 노드 쌍의 개수를 반환한다.
    # 1. 두 노드는 leaf 노드여야 한다.
    # 2. 두 노드 사이의 거리는 distance 이하여야 한다.

    # 문제 해결방법: Brute Force
    # 1. 노드의 거리를 계산하는 함수를 작성한다.
    # 2. 모든 leaf 노드 쌍을 찾는다.
    # 3. 두 노드 사이의 거리를 계산한다. => how?

    # 두 노드 사이의 거리를 계산하는 함수
    # 1. 두 노드의 공통 조상을 찾는다.
    # 2. 두 노드의 공통 조상을 기준으로 두 노드 사이의 거리를 계산한다.
    # => loop를 돌면서 조상을 기록한다. but 이 node는 그걸 지원하지 않는 구조이므로 별개의 자료구조를 사용해야 한다.
    def countPairs(self, root: TreeNode, distance: int) -> int:

        result = 0

        dict_parent_node = {root: None}
        leaf_nodes = []

        def dfs(node):

            if not node.left and not node.right:
                leaf_nodes.append(node)
                return

            if node.left:
                dict_parent_node[node.left] = node
                dfs(node.left)
            if node.right:
                dict_parent_node[node.right] = node
                dfs(node.right)
        
        dfs(root)

        for i in range(len(leaf_nodes)):
            for j in range(i + 1, len(leaf_nodes)):
                left_node = leaf_nodes[i]
                right_node = leaf_nodes[j]

                left_node_ancestors = []
                right_node_ancestors = []

                while left_node:
                    left_node_ancestors.append(left_node)
                    left_node = dict_parent_node.get(left_node)
                
                while right_node:
                    right_node_ancestors.append(right_node)
                    right_node = dict_parent_node.get(right_node)
                
                common_ancestor = None
                for left_distance, left_ancestor in enumerate(left_node_ancestors):
                    for right_distance, right_ancestor in enumerate(right_node_ancestors):
                        if left_ancestor == right_ancestor:
                            common_ancestor = left_ancestor
                            common_distance = left_distance + right_distance

                            if common_distance <= distance:
                                result += 1
                            break
                    if common_ancestor:
                        break

        return result

if __name__ == '__main__':
    sample = Solution()
    root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))

    sample.countPairs(root, 3) # 1