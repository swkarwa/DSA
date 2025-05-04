from importlib.util import source_hash


class Pair:
    def __init__(self, node: int, path: str):
        self.node = node
        self.path = path


class Solution:

    def print_graph_bfs(self, n, graph):
        visited = [False] * n
        # s1 add source to q
        p = Pair(0, "0")
        q = list()
        q.append(p)
        result = []
        while(q):
            top = q.pop(0)
            if(visited[top.node]):
                continue
            visited[top.node] = True
            print(top.path)
            for nbr in graph[top.node]:
                if(not visited[nbr]):
                    q.append(Pair(nbr , top.path+str(nbr)))
graph = [
    [1, 3],
    [2, 0],
    [1, 3],
    [0, 4, 2],
    [3, 5, 6],
    [ 4, 6],
    [5, 4]
]
s = Solution()
s.print_graph_bfs(len(graph), graph)
