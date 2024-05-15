//https://leetcode.com/problems/power-of-two/description/

function isPowerOfTwo(n: number): boolean {
    if (n < 1) return false;

    while (n > 1) {
        if (n % 2 !== 0) return false;
        n = n / 2;
    }

    return true;
};
