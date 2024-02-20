# Problem: Thorns and Coins
# 가시와 동전이 있는 길이 주어질 때, 동전을 최대한 많이 얻을 수 있는 동전의 개수를 구하는 문제
# 가시는 *, 동전은 @, 빈 공간은 .으로 표시된다.
# 이동할 수 있는 칸수는 1칸 또는 2칸이다.
# 가시가 있는 칸에는 이동할 수 없다.
# 동전이 있는 칸에 도착하면 동전을 얻을 수 있다.
# 가시가 2개 연속으로 있을 경우 이를 뛰어넘을 수 없으므로, 가시가 도착하기 전까지 획득 가능한 최대 동전의 개수를 구해야 한다.
def max_coins(path: str) -> int:
    n = len(path)
    dp = [0] * (n + 2)
    end = n
    for i in range(n):
        if i < n - 1 and path[i] == '*' and path[i + 1] == '*':
            return max(dp[i + 1], dp[i])
        
        dp[i + 2] = max(dp[i + 1], dp[i]) + (path[i] == '@')
    return dp[-1]


if __name__ == "__main__":
    num_test_case = int(input().strip())
    list_path = []

    for _ in range(num_test_case):
        n = int(input().strip())
        list_path.append(input().strip())
    
    for path in list_path:
        print(max_coins(path))