from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def get_path(graph, src, current):

            if (src == len(graph) - 1):
                result.append(current[:])

            for nbr in graph[src]:
                current.append(nbr)
                get_path(graph, nbr, current)
                current.pop()

        result = []
        get_path(graph, 0, [0])
        return result


result = Solution().allPathsSourceTarget([[1, 2], [3], [3], []])
print(result)
