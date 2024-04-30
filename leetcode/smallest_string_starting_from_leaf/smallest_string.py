# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search_whole_tree(self, current_node, current_str = "", smallest_str = ""):

        print(current_node.val)
        if (current_str == ""):
            current_str += chr(ord('a') + current_node.val)


        current_left_node = current_node.left
        
        if (current_left_node != None):
            left_node_str = chr(ord('a') + current_left_node.val) + current_str
            smallest_str = self.search_whole_tree(current_left_node, left_node_str, smallest_str)


        current_right_node = current_node.right

        if (current_right_node != None):
            right_node_str = chr(ord('a') + current_right_node.val) + current_str
            smallest_str = self.search_whole_tree(current_right_node, right_node_str, smallest_str)


        if ((current_left_node == None) and (current_right_node == None)):
            if ((current_str <= smallest_str) or (smallest_str == "")):
                return current_str

        return smallest_str


    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return self.search_whole_tree(root)
