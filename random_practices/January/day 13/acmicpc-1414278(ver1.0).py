# https://www.acmicpc.net/problem/14278


## 우선은 아래가 견실한지 여부에 대해서는 고려하지 않은 ver 1.0을 작성하도록 한다.

class BlockPlacement:
    def __init__(self, width, height):
        # self.placement_matrix[x][y]는 (x,y)좌표에 가로의 형태로 1x1, 2x1, 3x1 block
        # 중 임의의 것의 right_most vertex가 놓였을 때의 경우의 수를 나타낸다.
        self.placement_matrix = [[0] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.block_sizes = [1, 2, 3]
    

    # dynamic programming 방법을 통해 (0,0) ~ (w, h)까지를 순회하면서 self.placement_matrix 값을 
    # 초기화할 함수
    def initializePlacementMatrix(self):
        # TODO
        # w, h가 0인 경우에 대해서는 어떻게 생각해야 할까?
        # 예를 들어 (3,1)의 최대 사이즈에 대해 해당 값을 연산하려 한다 하자.
        # 그렇다면 (3,1) 좌표에 길이 3짜리 block이 놓이는 경우 한가지가 존재하고, 이는 (3 - 3, 1)의 좌표에
        # 있는 dp 값을 참조해서 계산해야 한다. 즉
        # (0,1)값은 1로 저장돼있어야한다는 이야기가 된다.
        # 그렇다면 x좌표가 0인 녀석들의 값은 1로 고정한다
        self.placement_matrix[0] = [1] * self.height
        # 이 부분은 처음에 constructor에서 포함해서 변경할 수 있는 개선점 중 하나이다. 값을 두번 할당하고 있음.

        for w in range(1, self.width):
            for h in range(1, self.height):
                for block_size in self.block_sizes:
                    if w - block_size < 0:
                        continue

                    self.placement_matrix[w][h] += self.placement_matrix[w - block_size][h]


    # size가 x, y인 frame에 대한 경우의 수를 계산하는 method
    def count_ways(self, x, y):
        # 아직 미구현이므로 미구현 상태임을 알리는 출력을 내보내자
        return "Not implemented"

        if y < 0:
            return 0
        
        # TODO
        # Base case는 무엇인가? y == 0, x == 0일 때에 대한 처리는 어떻게 해야하는가?
        # 예를 들어 count_ways(0, 0), count_ways(1,0), count_ways(2,0)
        # count_ways(0, 1), count_ways(0, 2)의 값은 어떻게 처리해야 하는가? 이 경우는
        # 폭/높이가 존재하지 않지만, 옆에 블록을 놓았을 경우에 참고해야 할 값들이다.
        # 라는 것이 최초의 생각이었지만, 이것은 placement_matrix[0][1]에서 고려해야 할 것들이고,
        # count_ways(0, 1)은 해당의 경우의 수를 원하는 것이므로 이는 단순하게 y == 0일 때는 1을
        # return하면 되는데, 이는 문제에서 제시하는 아무 것도 없는 상태는 1가지로 주어지기 때문이다.
        if y == 0:
            return 1
        
        if x == 0:
            return 0
        
        # 현재 방식의 문제는 결국 placement_matrix가 초기화가 돼있는지 여부를 count_ways를 통해 유기적으로 점검하는
        # 깔끔한 형태의 코드가 나오지 않았다는 점이다. 이 부분은 현재 두 가지로 해결할 수 있는데 하나는 현재
        # 재귀함수 형태를 포기하고 iterative method의 형태로 수정하는 것, 혹은 처음에 matrix를 -1로 초기화 한 이후에,
        # -1일 경우에 해당 값을 연산하도록 하면 된다.
        # 그런데 이 문제는 어차피 최종의 값을 연산 할 때 이전의 결과 값 중에 필요로 하지 않는 subsolution이 존재하지 않는다.
        # 그렇다면 count_ways는 단순히 x,y지점이 우상단 최고의 좌표일 때의 경우의 수 합을 구하도록 하는 연산 알고리즘을 작성하고
        # placement_matrix를 (0,0) ~ (weight, height)까지 초기화하는 함수를 작성한 뒤, object를 할당했을 때
        # 연산하도록 구현하는 것이 용이할 것으로 보인다.


if __name__ == "__main__":
    list_input_sizes = [(1, 3), (3, 1), (3, 2), (4, 9), (5, 5)]

    for w, h in list_input_sizes:
        sample_object = BlockPlacement(w, h)
        print(sample_object.count_ways(w, h))