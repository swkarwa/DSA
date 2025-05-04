from collections import deque
from typing import Optional
from typing import List

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def get_width(self, root, min_max, hd):
        if not root: return

        min_max[0] = min(hd, min_max[0])
        min_max[1] = max(hd, min_max[1])

        self.get_width(root.left, min_max, hd - 1)
        self.get_width(root.right, min_max, hd + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_max = [float('inf'), float('-inf')]
        self.get_width(root, min_max, 0)
        total_size = min_max[1] - min_max[0] + 1

        result = [[] for _ in range(total_size)]
        q = deque()
        q.append((abs(min_max[0]), root))

        while (q):
            size = len(q)
            for _ in range(size):
                hd, node = q.popleft()
                result[hd].append(node.val)

                if (node.left):
                    q.append((hd - 1, node.left))

                if (node.right):
                    q.append((hd + 1, node.right))

        return result