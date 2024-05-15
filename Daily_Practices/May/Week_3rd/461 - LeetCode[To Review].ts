// https://leetcode.com/problems/hamming-distance/

function hammingDistance(x: number, y: number): number {
    let binaryX = x.toString(2);
    let binaryY = y.toString(2);
    let maxLength = Math.max(binaryX.length, binaryY.length);

    binaryX = binaryX.padStart(maxLength, '0');
    binaryY = binaryY.padStart(maxLength, '0');

    let count = 0;

    for (let i = 0; i < maxLength; i++) {
        count += parseInt(binaryX[i]) ^ parseInt(binaryY[i]);
    }

    return count;
};
