# https://school.programmers.co.kr/learn/courses/30/lessons/178871

from typing import List

def solution(players: List[str], callings: List[str])->List[str]:
    player_rank, rank_player = {}, {}
    for rank, player in enumerate(players):
        player_rank[player] = rank
        rank_player[rank] = player
    
    for player in callings:
        if player in player_rank:
            current_rank = player_rank[player]
            front_player = rank_player[current_rank - 1]

            player_rank[player] -= 1
            player_rank[front_player] += 1

            rank_player[current_rank] = front_player
            rank_player[current_rank - 1] = player
    
    answer = [rank_player[rank] for rank in range(len(players))]

    return answer