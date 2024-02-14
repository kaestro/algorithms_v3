# https://leetcode.com/problems/network-delay-time/description/

from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    # weighted_edges[i] = (source_idx, target_idx, weight) where weight is the time it takes
    # to go from source_idx to target_idx
    # return the minimum time it takes to go from the source node to all other nodes
    # if it is impossible to go from the source node to all other nodes, return -1
    def networkDelayTime(self, weighted_edges: List[List[int]], num_nodes: int, source_node_idx: int) -> int:
        # Create graph
        graph = defaultdict(dict)
        for source_idx, target_idx, weight in weighted_edges:
            graph[source_idx][target_idx] = weight
    
        # Initialize distances as infinity for all nodes since we don't know the shortest path yet
        min_network_delays = {i: float('inf') for i in range(1, num_nodes + 1)}
        min_network_delays[source_node_idx] = 0

        # Initialize priority queue with the source node
        priority_queue = [(0, source_node_idx)]

        # Dijkstra's algorithm
        while priority_queue:
            current_delay, current_node = heappop(priority_queue)
            if current_delay > min_network_delays[current_node]:
                continue
            for neighbor, weight in graph[current_node].items():
                total_delay = current_delay + weight
                if total_delay < min_network_delays[neighbor]:
                    min_network_delays[neighbor] = total_delay
                    heappush(priority_queue, (total_delay, neighbor))
        
        # If there is a node that we can't reach, return -1
        if float('inf') in min_network_delays.values():
            return -1
        else:
            return max(min_network_delays.values())