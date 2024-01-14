# https://www.acmicpc.net/problem/14278

# TODO
# 길이가 3인 블록을 추가할 때의 예외 사항에 대한 처리
# 가운데 빈 경우는 아직 고려하지 않고 생각해보자

class BlockPlacement:
    def __init__(self, width, height):
        # dp는 (넓이, 높이)일 때 해당 상황에 가능한 모든 경우의 수를 저장한 자료구조이다.
        self.dp = {}
        self.width = width
        self.height = height


    def count_ways(self, x, y):
        # 기저 사례: y좌표가 음수인 경우, 블록을 놓을 수 없음
        if y < 0:
            return 0

         
        ## if y == 0:
        ##    return 1
        
        if y > self.height or x > self.width:
            return -1
        
        # 기저 사례: 블록을 모두 놓았을 때, 하나의 경우가 추가됨
        if x == 0:
            return 1
        
        ways = 0

        # 블록을 놓지 않는 경우
        if y > 0:
            ways += self.count_ways(x, y - 1)

        # 가로로 길이 1인 블록을 놓는 경우
        ways += self.count_ways(x - 1, y)
        
        # 가로로 길이 2인 블록을 놓는 경우
        if x > 1:
            ways += self.count_ways(x - 2, y)
        
        if x > 2:
            ways += self.count_ways(x - 3, y)

        self.dp[(x,y)] = ways

        return ways



if __name__ == "__main__":
    # w, h = map(int, input().split())
    ListWH = [(1, 3), (3, 1), (3, 2), (4, 9), (5, 5)]
    for w, h in ListWH:
        SampleBlock = BlockPlacement(w,h)
        print(SampleBlock.count_ways(w,h))
        print("hello")