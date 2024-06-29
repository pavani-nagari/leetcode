from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = {i: 0 for i in range(n)}
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1      
        sorted_cities = sorted(degree, key=degree.get, reverse=True)
        value_assignment = {}
        value = n
        for city in sorted_cities:
            value_assignment[city] = value
            value -= 1
        total_importance = 0
        for road in roads:
            total_importance += value_assignment[road[0]] + value_assignment[road[1]]
        return total_importance


