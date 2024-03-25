from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        triangle = [[1] * row for row in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        return triangle


if __name__ == "__main__":
    listNumRows = [5, 1]
    for numRows in listNumRows:
        print(Solution().generate(numRows))