class TreeNode:
    def __init__(self , val = 0 , left=None , right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, pre_order , in_order):
        if(not pre_order or not in_order):
            return None

        root_val = pre_order[0]
        root_node = TreeNode(root_val)
        io_idx = in_order.index(root_val)

        root_node.left = self.buildTree(pre_order[1:io_idx+1] , in_order[:io_idx])
        root_node.right = self.buildTree(pre_order[io_idx + 1:], in_order[io_idx+1:])

        return root_node

    def print_tree(self, root:TreeNode):
        if(not root):

            return [None]
        result = [root.val]
        result += self.print_tree(root.left)
        result += self.print_tree(root.right)
        return result

in_order = [9,3,15,20,7]
pre_order = [3,9,20,15,7]
root = Solution().buildTree(pre_order , in_order)

result = Solution().print_tree(root)
print(result)