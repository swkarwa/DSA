from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if (not inorder or not postorder):
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        idx = inorder.index(root_val)


        root.right = self.buildTree(inorder[idx + 1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)



        return root

Solution().buildTree([9,3,15,20,7] , [9,15,7,20,3])