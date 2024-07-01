# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_is_checked = True
        if root.left:
            left_is_checked = self.check(root.left, False, 0, True, root.val)

        right_is_checked = True
        if root.right:
            right_is_checked = self.check(root.right, True, root.val, False, 0)

        if (left_is_checked and right_is_checked):
            return True
        return False

    def check(self, node, has_min, min_val, has_max, max_val):
        if (has_max and node.val >= max_val):
            return False
        if (has_min and node.val <= min_val):
            return False

        left_is_checked = True
        if node.left:
            left_is_checked = self.check(node.left, has_min, min_val, True, node.val)

        right_is_checked = True
        if node.right:
            right_is_checked = self.check(node.right, True, node.val, has_max, max_val)

        if (left_is_checked and right_is_checked):
            return True

        return False
