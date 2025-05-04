class Node:
    def __init__(self , val):
        self.left = None
        self.right = None
        self.data = val

class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        top_map = dict()
        self.view(root, top_map, 0, 0)
        top_map = dict(sorted(top_map.items()))

        return [val for key, (val, _) in top_map.items()]

    def view(self, root, top_map, level, hd):
        if (not root):
            return

        if hd not in top_map or level < top_map[hd][1]:
            top_map[hd] = (root.data, level)

        self.view(root.left, top_map, level + 1, hd - 1)
        self.view(root.right, top_map, level + 1, hd + 1)

# build tree
# Custom tree build to test the case
n = Node(10)
n.left = Node(20)
n.right = Node(30)
n.left.left = Node(40)
n.left.right = Node(60)
n.left.right.left = Node(100)  # Node at a deeper level
n.right.right = Node(90)

# Instantiate Solution and call topView
print(Solution().topView(n))

Solution().topView(n)