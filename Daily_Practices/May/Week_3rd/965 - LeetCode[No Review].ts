// https://leetcode.com/problems/univalued-binary-tree/description/


//Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


function isUnivalTree(root: TreeNode | null): boolean {
    if (!root) {
        return false;
    }

    const rootValue = root?.val;
    let stack: TreeNode[] = [root];

    while (stack.length > 0) {
        let node = stack.pop();
        if (node?.val !== rootValue) {
            return false;
        }
        if (node.left) {
            stack.push(node.left);
        }
        if (node.right) {
            stack.push(node.right);
        }
    }

    return true;
};
