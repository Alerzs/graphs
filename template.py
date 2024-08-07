import json
import csv
from collections import defaultdict, deque
import heapq

class Graph:


    def __init__(self ,file) -> None:
        
        pass
        

    def yaal_count(self):
     pass

    def ras_count(self):
        pass
    


    def BFS(self, start):
        if self.type == "weighted":
            print("BFS is not allowed for weighted graphs")
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(neighbor for neighbor, _ in self.adjacency_list[vertex] if neighbor not in visited)

        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor, _ in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

            dfs_recursive(start)
        return result

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
class Yaal:
    
    def __init__(self ,org ,des ,weight) -> None:
        self.org = org
        self.des = des
        self.weight = weight
