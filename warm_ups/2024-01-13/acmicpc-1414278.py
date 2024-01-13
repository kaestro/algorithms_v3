# https://www.acmicpc.net/problem/14278

# 입력받기
w, h = map(int, input().split())

# dp 배열 초기화
# width, h의 위치에 1, 2, 3 사이즈 블록의 시작부분이 놓일 수 있는
# 경우의 수를 저장하는 자료구조
dp = [[[0] * 3 for _ in range(h)] for _ in range(w)]

block_sizes = [1, 2, 3]

for width in range(w):
    for height in range(h):
        for blocks in range(3):
            continue
