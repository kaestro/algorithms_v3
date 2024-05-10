# https://school.programmers.co.kr/learn/courses/30/lessons/176963

from typing import List
from collections import defaultdict

def solution(names, yearnings, photoes_list: List[List[str]]):
    name_yearning = defaultdict(int)
    for name, yearning in zip(names, yearnings):
        name_yearning[name] = yearning

    answer = []
    for photoes in photoes_list:
        score = 0
        for photo in photoes:
            score += name_yearning[photo]
        answer.append(score)

    return answer