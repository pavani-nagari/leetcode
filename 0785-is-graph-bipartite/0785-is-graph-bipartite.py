from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # Use -1 for uncolored, 0 for one color, and 1 for the other color

        def bfs(start):
            queue = deque([start])
            color[start] = 0  # Start coloring the starting node with 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Color with opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # If the neighbor has the same color, it's not bipartite
                        return False
            return True

        for i in range(n):
            if color[i] == -1:  # If not colored, start a BFS
                if not bfs(i):
                    return False
        
        return True


                
            
            
        
        