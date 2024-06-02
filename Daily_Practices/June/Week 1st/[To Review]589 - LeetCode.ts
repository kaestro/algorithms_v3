class Node {
    val: number
    children: Node[] | undefined
    constructor(val?: number) {
        this.val = (val===undefined ? 0 : val)
        this.children = []
    }
}


function preorder(root: Node | null): number[] {
    let result: number[] = [];
    if (root === null) {
        return result;
    }

    let stack: Node[] = [root];

    while (stack.length > 0) {
        let node = stack.pop() as Node;
        result.push(node.val);
        if (node.children) {
            for (let i = node.children.length - 1; i >= 0; i--) {
                stack.push(node.children[i]);
            }
        }
    }

    return result;
};
