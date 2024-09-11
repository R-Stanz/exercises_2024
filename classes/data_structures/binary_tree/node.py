class Node:
    left_son = None
    right_son = None

    def __init__(self, value, sub_tree_height = 1):
        self.value = value
        self.sub_tree_height = sub_tree_height

    def add_son(self, value):
        if self.left_son:
            if self.right_son:
                return False
            self.right_son = Node(value)
        else:
            self.left_son = Node(value)

        return True

    def min_sub_tree(self):
        left_sub_tree_height, right_sub_tree_height = self.sub_trees_heights()

        if left_sub_tree_height <= right_sub_tree_height:
            return self.left_son
        else:
            return self.right_son
    
    def update_sub_tree_height(self):
        self.sub_tree_height = 1

        left_sub_tree_height, right_sub_tree_height = self.sub_trees_heights()

        self.sub_tree_height += max(left_sub_tree_height, right_sub_tree_height)

    def sub_trees_heights(self):
        left_sub_tree_height = 0
        if self.left_son:
            left_sub_tree_height = self.left_son.sub_tree_height
        right_sub_tree_height = 0
        if self.right_son:
            right_sub_tree_height = self.right_son.sub_tree_height

        return (left_sub_tree_height, right_sub_tree_height)

    def __repr__(self):
        return "\n\tNode Value: {}, Sub-Tree Height: {}".format(self.value, self.sub_tree_height)
