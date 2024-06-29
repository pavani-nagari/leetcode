from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Calculate the degree of each city
        degree = {i: 0 for i in range(n)}
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        
        # Step 2: Sort cities by degree in descending order
        sorted_cities = sorted(degree, key=degree.get, reverse=True)
        
        # Step 3: Assign values based on degree
        value_assignment = {}
        value = n
        for city in sorted_cities:
            value_assignment[city] = value
            value -= 1
        
        # Step 4: Compute the total importance
        total_importance = 0
        for road in roads:
            total_importance += value_assignment[road[0]] + value_assignment[road[1]]
        
        return total_importance


