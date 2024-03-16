from typing import List

def matrixBlockSum(mat: List[List[int]], K: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    rangeSum = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            rangeSum[i + 1][j + 1] = rangeSum[i + 1][j] + rangeSum[i][j + 1] - rangeSum[i][j] + mat[i][j]

    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1, c1 = max(0, i - K), max(0, j - K)
            r2, c2 = min(m, i + K), min(n, j + K)
            res[i][j] = rangeSum[r2 + 1][c2 + 1] - rangeSum[r2 + 1][c1] - rangeSum[r1][c2 + 1] + rangeSum[r1][c1]

    return res