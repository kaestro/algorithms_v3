# https://leetcode.com/problems/path-with-maximum-probability/description/

from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    # edges[i] = [a, b] means the probability of success from node a to node b is succProb[i]
    def maxProbability(self, num_nodes: int, edges: List[List[int]], succProbability: List[float], start_node_idx: int, end_node_idx: int) -> float:
        # Create graph
        graph = defaultdict(dict)
        for i, (a, b) in enumerate(edges):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = succProbability[i]
            graph[b][a] = succProbability[i]
        
        # Dijkstra's algorithm
        maximum_probabilities = [0.0] * num_nodes
        maximum_probabilities[start_node_idx] = 1.0

        # (probability, node_idx)
        # it starts with a priority queue with the start node and its distance to itself
        # the distance is negative because the priority queue is a min heap and we want to pop the node with the highest distance
        # heapq.heappop() returns the smallest item, so we use negative distances to get the largest probability
        priority_queue = [(-1.0, start_node_idx)]
        while priority_queue:
            current_probability, node_idx = heappop(priority_queue)
            if node_idx == end_node_idx:
                return -current_probability
            for neighbor, edge_weight in graph[node_idx].items():
                next_probability = -current_probability * edge_weight
                if next_probability > maximum_probabilities[neighbor]:
                    maximum_probabilities[neighbor] = next_probability
                    heappush(priority_queue, (-next_probability, neighbor))

        # if we reach here, it means there is no path from start_node_idx to end_node_idx
        # therefore we return 0.0 for the probability of success is 0
        return 0.0


# Test cases
test = Solution()
assert test.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2) == 0.25