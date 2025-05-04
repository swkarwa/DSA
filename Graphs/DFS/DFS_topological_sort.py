# DFS topological sort
from typing import List


class Solution:
    def findOrder(self, courses: int, prereq: List[List[int]]) -> List[int]:
        visited = [False] * courses
        temp_mark = [False] * courses
        graph = [[] for _ in range(courses)]
        visited = [False] * courses
        stack = []
        for a, b in prereq:
            graph[a].append(b)

        for i in range(len(visited)):
            if (not visited[i]):
                if not self.dfs(graph, i, visited, temp_mark, stack):
                    return []
        return stack

    def dfs(self, graph, src, visited, temp_mark, stack):
        if (temp_mark[src]):
            return False

        if (visited[src]):
            return True

        temp_mark[src] = True

        for nbr in graph[src]:
            if (not visited[nbr]):
                if not self.dfs(graph, nbr, visited, temp_mark, stack):
                    return False

        temp_mark[src] = False
        visited[src] = True
        stack.append(src)

        return True


Solution().findOrder(2, [[0, 1]])

