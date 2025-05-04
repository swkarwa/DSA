"""

    Question : https://leetcode.com/problems/course-schedule/description/
    only representation of graph , solution not yet dont

"""
from typing import List


class Solution:
    def buildUndirectedGraphAsAdjList(self, numCourses: int, prerequisites: List[List[int]]):
        """
            numCourses : vertices
            prerequisites : edges

        """

        graph = [[] for _ in range(numCourses)]
        for source, destination in prerequisites:
            graph[source].append(destination)
            graph[destination].append(source)

        print(graph)

    def buildUndirectedGraphAsMatrix(self, numCourses: int, prerequisites: List[List[int]]):
        """
            numCourses : vertices
            prerequisites : edges

        """

        graph = [[0] * numCourses for _ in range(numCourses)]
        for s , d in prerequisites:
            graph[s][d] = 1
            graph[d][s] = 1

        for g in graph:
            print(g)

"""
input:
    numberOfCources : 4
    prerequisites : [[1,0] ,[2,0] , [2,1] , [3,1]]

"""

numberOfCources = 4
prerequisites = [[1, 0], [2, 0], [2, 1], [3, 1]]

s = Solution()
s.buildUndirectedGraphAsMatrix(numberOfCources, prerequisites)
s.buildUndirectedGraphAsAdjList(numberOfCources, prerequisites)
