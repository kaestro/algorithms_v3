#https://leetcode.com/problems/distribute-candies-among-children-i/description/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        cnt = 0

        for i in range(limit + 1):
            sum = 0
            if i > n:
                break

            for j in range(limit + 1):
                sum = i + j
                if sum == n:
                    cnt += 1
                    break
                elif sum > n:
                    break

                for k in range(limit + 1):
                    sum += k
                    if sum == n:
                        cnt += 1
                        sum -= k
                        break

                    sum -= k
        return cnt



    def distributeCandiesVer2(self, n: int, limit: int) -> int:
        cnt = 0

        for i in range(limit + 1):
            if i > n:
                break

            for j in range(limit + 1):
                sum = i + j - 1
                if sum >= n:
                    break

                for k in range(limit + 1):
                    sum += 1
                    if sum == n:
                        cnt += 1
                        break

        return cnt

    def distributeCandiesVer3(self, n: int, limit: int) -> int:
        cnt = 0

        for i in range(min(n, limit) + 1):
            for j in range(min(n - i, limit) + 1):
                k = n - i - j
                if k <= limit:
                    cnt += 1

        return cnt