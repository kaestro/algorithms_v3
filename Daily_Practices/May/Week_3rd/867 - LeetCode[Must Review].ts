// https://leetcode.com/problems/transpose-matrix/description/

function transpose(matrix: number[][]): number[][] {

    return matrix[0].map((_, i) => matrix.map(row => row[i]));
};
