# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if (depth == 1):
            return TreeNode(val, root)

        elif (depth == 2):
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, None, root.right)
            return root

        else:
            if (root.left != None):
                root.left = self.addOneRow(root.left, val, depth-1)
            if (root.right != None):
                root.right = self.addOneRow(root.right, val, depth-1)
            return root
