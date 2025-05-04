class Solution:
    """
        Hamiltonian Path: A path in a graph that visits each vertex exactly once.
        Hamiltonian Cycle: A cycle that visits each vertex exactly once and returns to the starting vertex.
    """

    def print_all_hamiltonian_path_and_cycle(self, n, graph):
        visited = [False] * n
        self.dfs(graph, 0, visited, [0], 0)

    def dfs(self, graph, src, visited, current, start_point):
        if (all(visited)):
            path = [str(node) for node in current]
            if (start_point in graph[current[-1]]):
                print("".join(path), "*")  # cycle
            else:
                print("".join(path), "#")  # path

        visited[src] = True
        for nbr in graph[src]:
            if (not visited[nbr]):
                visited[nbr] = True
                current.append(nbr)
                self.dfs(graph, nbr, visited, current, start_point)
                current.pop()
                visited[nbr] = False
        visited[src] = False


graph = [
    [1, 3],
    [2, 0],
    [1, 5, 3],
    [0, 4, 2],
    [3, 5, 6],
    [2, 4, 6],
    [5, 4]
]
s = Solution()
s.print_all_hamiltonian_path_and_cycle(len(graph), graph)
