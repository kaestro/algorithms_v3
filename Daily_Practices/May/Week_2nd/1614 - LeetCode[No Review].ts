// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

function maxDepth(s: string): number {
    let maxDepth = 0;
    let currentDepth = 0;
    for (let char of s) {
        if (char === '(') {
            currentDepth++;
            maxDepth = Math.max(maxDepth, currentDepth);
       } else if (char === ')') {
            currentDepth--;
        }
    }
    return maxDepth;
};
