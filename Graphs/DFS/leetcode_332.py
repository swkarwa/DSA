from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Prepare graph as an adjacency list, sorting each list lexicographically
        graph = defaultdict(list)

        for frm, to in sorted(tickets, reverse=True):
            graph[frm].append(to)

        result = []
        self.dfs("JFK", graph, result)
        return result[::-1]  # Reverse the result to get the correct order

    def dfs(self, frm_city, graph, result):
        # Explore all destinations from the current city
        while graph[frm_city]:
            next_city = graph[frm_city].pop()
            self.dfs(next_city, graph, result)

        # Append city to result after all connections are visited
        result.append(frm_city)

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))