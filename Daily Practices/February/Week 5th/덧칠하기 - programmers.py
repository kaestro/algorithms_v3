from typing import List

def solution(wall_length: int, roller_length: int, section_list: List[int]) -> int:
    answer = 0
    section_dict = {section - 1: 1 for section in section_list}

    for section in sorted(section_dict):
        if section_dict[section] == 0:
            for i in range(section, min(section + roller_length, wall_length)):
                if i in section_dict:
                    section_dict[i] = 1
            answer += 1

    return answer


import heapq

def solution_heap(wall_length: int, roller_length: int, section_list: List[int]) -> int:
    answer = 0
    section_heap = section_list.copy()
    heapq.heapify(section_heap)

    while section_heap:
        min_section = heapq.heappop(section_heap)
        answer += 1
        section_heap = [i for i in section_heap if i >= min_section + roller_length]
        heapq.heapify(section_heap)

    return answer