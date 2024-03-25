from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    # edge is bidirectional
    # elements in edges are [from_node_idx, to_node_idx, weight]
    # distanceThreshold is the maximum distance between two nodes
    # return the city with the smallest number of neighbors at a threshold distance
    # if there are multiple cities with the same smallest number of neighbors, return the city with the greatest city index

    # Dijkstra's algorithm for each node
    def findTheCity(self, num_cities: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # create a directed graph
        city_graph = defaultdict(list)
        for edge in edges:
            city_graph[edge[0]].append((edge[1], edge[2]))
            city_graph[edge[1]].append((edge[0], edge[2]))
        
        # initialize the distance matrix
        distance = [[float('inf') for _ in range(num_cities)] for _ in range(num_cities)]

        # fill the distance matrix using Dijkstra's algorithm
        for start_node_idx in range(num_cities):
            distance[start_node_idx][start_node_idx] = 0
            min_distance_heap = [(0, start_node_idx)]
            while min_distance_heap:
                current_node_distance, current_node_idx = heappop(min_distance_heap)
                for next_node_idx, next_node_distance in city_graph[current_node_idx]:
                    if current_node_distance + next_node_distance < distance[start_node_idx][next_node_idx]:
                        distance[start_node_idx][next_node_idx] = current_node_distance + next_node_distance
                        heappush(min_distance_heap, (distance[start_node_idx][next_node_idx], next_node_idx))
        
        # count the number of neighbors at a threshold distance
        min_neighbors = float('inf')
        min_neighbors_city_idx = -1
        for from_city_idx in range(num_cities):
            neighbors = 0
            for to_city_idx in range(num_cities):
                if distance[from_city_idx][to_city_idx] <= distanceThreshold:
                    neighbors += 1
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                min_neighbors_city_idx = from_city_idx

        return min_neighbors_city_idx
    

    def floydWarshallFindTheCity(self, num_cities: int, edges: List[List[int]], distanceThreshold: int) -> int:
        city_graph = defaultdict(list)
        for edge in edges:
            city_graph[edge[0]].append((edge[1], edge[2]))
            city_graph[edge[1]].append((edge[0], edge[2]))
        
        min_neighbors = float('inf')
        min_neighbors_city_idx = -1
        for start_node_idx in range(num_cities):
            distances = [float('inf')] * num_cities
            distances[start_node_idx] = 0
            min_distance_heap = [(0, start_node_idx)]
            while min_distance_heap:
                current_node_distance, current_node_idx = heappop(min_distance_heap)
                for next_node_idx, next_node_distance in city_graph[current_node_idx]:
                    if current_node_distance + next_node_distance < distances[next_node_idx]:
                        distances[next_node_idx] = current_node_distance + next_node_distance
                        heappush(min_distance_heap, (distances[next_node_idx], next_node_idx))
            
            neighbors = sum(d <= distanceThreshold for d in distances)
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                min_neighbors_city_idx = start_node_idx

        return min_neighbors_city_idx