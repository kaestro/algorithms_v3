# https://school.programmers.co.kr/learn/courses/30/lessons/258711


def solution(edges):
    answer = []

    graph = create_graph_from_edges(edges)
    num_loops = count_loops(graph)

    print("도넛의 갯수는 " + str(num_loops) + "입니다")

    return answer

def create_graph_from_edges(edges):
    graph = {}

    for edge in edges:
        starting_node, ending_node = edge
        if starting_node not in graph:
            graph[starting_node] = []
        if ending_node not in graph:
            graph[ending_node] = []
        graph[starting_node].append(ending_node)
    return graph

def count_loops(graph):
    loop_count = 0
    visited = set()

    for node in graph:
        if node not in visited:
            stack = [node]
            loop_nodes = set()

            while stack:
                current = stack.pop()

                if current in loop_nodes:
                    continue

                loop_nodes.add(current)

                for neighbor in graph[current]:
                    stack.append(neighbor)
                
                if current in visited:
                    loop_count += 1
    
    return loop_count

def isDonut(edges):
    return False


def isStick(edges):
    return False


def isEight(edges):
    return False

if __name__ == "__main__":
    edges_list = [
        [[2, 3], [4, 3], [1, 1], [2, 1]],
        [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11],
            [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]	
    ]

    answers_list = [ [2, 1, 1, 0], [4, 0, 1, 2] ]

    for edges in edges_list:
        solution(edges)

    print("테스트 코드입니다")