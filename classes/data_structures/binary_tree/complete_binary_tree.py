from node import Node

class CompleteBinaryTree:
    root = None
    def __init__(self):
        pass

    def add(self, value):
        if not self.root:
            self.root = Node(value)

        self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
        if not node.add_son(value):
            son = node.min_sub_tree()
            self.add_recursive(son, value)

        node.update_sub_tree_height()

    def min_value(self):
        if self.root:
            return self.min_value_recursion(self.root)
        print("The Tree Is Still Empty")

    def min_value_recursion(self, node):
        min_value = node.value

        if node.left_son:
            left_min = self.min_value_recursion(node.left_son)
            if min_value > left_min:
                min_value = left_min

        if node.right_son:
            right_min = self.min_value_recursion(node.right_son)
            if min_value > right_min:
                min_value = right_min

        return min_value

    def max_value(self):
        if self.root:
            return self.max_value_recursion(self.root)
        print("The Tree Is Still Empty")

    def max_value_recursion(self, node):
        max_value = node.value

        if node.left_son:
            left_max = self.max_value_recursion(node.left_son)
            if max_value < left_max:
                max_value = left_max

        if node.right_son:
            right_max = self.max_value_recursion(node.right_son)
            if max_value < right_max:
                max_value = right_max

        return max_value

    def in_order_ls(self, node, ls = []):
        if node.left_son:
            ls = self.in_order_ls(node.left_son, ls)

        ls.append(str(node))

        if node.right_son:
            ls = self.in_order_ls(node.right_son, ls)

        return ls

    def __repr__(self):
        nodes = []
        if self.root:
            nodes += self.in_order_ls(self.root)

        if nodes:
            nodes[-1] += "\n"

        msg = "["
        for node in nodes:
            msg += node
        msg += "]"

        return msg
