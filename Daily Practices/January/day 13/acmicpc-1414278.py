# https://www.acmicpc.net/problem/14278

# TODO
# 길이가 3인 블록을 추가할 때의 예외 사항에 대한 처리
# 가운데 빈 경우는 아직 고려하지 않고 생각해보자

class BlockPlacement:
    def __init__(self, width, height):
        # dp는 (넓이, 높이)일 때 해당 상황에 가능한 모든 경우의 수를 저장한 자료구조이다.
        # => 이 자료구조 설정이 옳은가? 해당 위치에 길이 1, 2, 3의 블록이 '시작하게' 놓이거나,
        # 끝나게 놓이도록 설정하는게 맞지 않은가?
        # => 이런 생각을 통해 선택한 dp 혹은 memo는 기존의 것과 어떤 차이를 보이는가?

        # 기존의 것이 가지고 있는 문제점은, 이전에 가능한 모든 경우의 수가 이후의 형태를 확정지어주지 못한다는 점이다.
        # ex) dp[(5, 2)]를 구하려 한다 하자. 그렇다면 현재 dp[(4,2)], dp[(3, 2)], dp[(2, 2)]를 고려해서 dp[(2, 2)] 뒤에다가
        # 1개짜리를 놓는 경우의수, dp[(3,2)] 뒤에다가 1, 2개짜리를 놓는 경우, dp[(1,2)] 뒤에다가 1, 2, 3개짜리를 놓는게 된다.
        # 그런데 dp[(1,2)]의 뒤에다가 1을 놓은 것은 결국 dp[(2,2)]에다가 중첩해서 존재하게 되고, 이는 중복해서 계산하는 결과를 낳게 된다.
        # 문제는 그러면 문제의 답보다 큰 값이 나와야하는데, 정작 더 작은 값이 나오고 있는 이유는 무엇일까?
        
        # dp의 optimal substructure라고 할 수 있는 overlapping problem이 무엇인지부터 명확하게 점검하는게 맞는가?
        # 현재 형태는 어느 것을 optimal substructure라고 가정하고 있는 것인가?
        # 현재는 원하는 형태보다 작은 크기의 블록이 존재할 수 있는 frame에서 존재할 수 있는 모든 경우의 수를 현재를 통해 답을 구하려 하고 있다.

        # 그럼 더 simplify해서, 내가 풀고자 하는 예를 들어 count_ways(3, 2)의 문제를 구하고자 한다고 하자. 이 것을 알기 위해 내가 알아야 하는
        # substructure들은 무엇이 있는가?
        # 이 경우에 이전의 형태와 다르게 '새로' 생성되는 경우의 수는 이와 작은 경우와 비교했을 때 알 수 있을 것이다.
        # count_ways(2,2)와 비교하면 이는 이제 가로에 한 줄이 새로 추가된 형태가 존재한다. column이 하나 더 늘었고 그러면 
        # 여기에 '끝나는' 새로운 블럭이 존재할 가능성이 생겼단 것이다.
        # 즉, (3,2)위치에 size 1, 2, 3짜리 block이 놓이는 경우의 수가 이전과 비교했을 때 새로 생겨난 것이다.
    
        # 그렇다면 size 3짜리 block이 있을 때, 이는 subproblem을 통해 답을 구할 수 있는가? 그렇다. 이는 (3,2) 좌표에 3짜리 block을 놓기 위해
        # 마지막에 놓이는 block의 위치를 제한한 경우의 수를 모두 합한 것을 통해 구할 수 있다. 3짜리 block은 (1,2), (2,2), (3,2)
        # 세 좌표를 차지하게 되고, 그러면 size 1, 2, 3짜리 block의 right vertex가 이 (0, 2)에 놓인 모든 경우의 수에 대해 size 3짜리
        # block이 존재할 수 있는 경우의 수를 구할 수 있다.

        # 마찬가지로 size 2짜리 block은 (1,2)에 size 1, 2, 3짜리 block의 right vertex가 놓였을 경우, size 1짜리 block은
        # (2,2)에 size 1, 2, 3 짜리 block의 right vertex가 놓였을 경우의 값을 통해 구할 수 있다.

        # 여기서 의문인 점은 이제 두가지이다.
        # 1. 현재 구해내고 있는 값은 이전과 비교해서 '새로 생겨난 경우의 수'들인데 그렇다면 우리가 원하는 모든 경우의 수의 합은
        # 어떻게 구해낼 것인가?
        # 2. 현재 어떤 block이든 상관없이 right_most_vertex의 위치가 놓으려하는 new_vertex_index - block_size에 block의
        # right_most_vertex가 놓여있는 경우의 수를 통해 새로운 vertex가 추가 됐을 때의 new case를 연산하고 있다. 그렇다면
        # 현재 dp[(x,y)][block_size]의 형태로 데이터를 저장하고자 하는 것은 무의미한 것이 아닌가?
        # => 그런 것으로 보인다.
        # 그렇다면 dp[(x,y)] 혹은 dp[x][y]는 심플하게 (x,y) 좌표에 해당 row에 놓인 임의의 block에 대한 right_most_vertex
        # 라고 생각하고 문제를 해결하려 하면 되지 않을까?
        # 이에 맞춰서 ver 1.0 코드를 작성해보자
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

        if (x, y) in self.dp:
            return self.dp[(x,y)]
        
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