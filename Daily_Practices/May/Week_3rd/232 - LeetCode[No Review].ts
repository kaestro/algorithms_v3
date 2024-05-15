//https://leetcode.com/problems/power-of-two/description/

function isPowerOfTwo(n: number): boolean {
    while (n > 1) {
        if (n % 2 !== 0) return false;
        n = n / 2;
    }
};
