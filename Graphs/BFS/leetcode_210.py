from typing import List
from collections import deque
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Create the graph and the in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        # Step 2: Populate the graph and in-degree array
        for a, b in prerequisites:
            graph[b].append(a)  # b must be taken before a
            in_degree[a] += 1  # Increase in-degree for a

        # Step 3: Initialize the queue with courses having zero in-degree
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        result = []

        # Step 4: Process the courses in topological order
        while q:
            course = q.popleft()
            result.append(course)

            # Decrease in-degree of neighbor courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # Step 5: Check if we were able to take all courses
        if len(result) == numCourses:
            return result
        else:
            return []  # Cycle detected, impossible to finish all courses


# Example usage:

Solution().findOrder(4 , [[1,0],[2,0],[3,1],[3,2]])