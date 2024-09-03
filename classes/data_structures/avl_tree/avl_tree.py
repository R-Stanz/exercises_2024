from node import Node

class Avl_tree:
    root = None
    def __init__ (self):
        pass

    def add(self, value):
        print("Adding: " + str(value))
        self.root = self.avl_add(self.root, value)

    def avl_add(self, node, value):
        if not node:
            return Node(value)

        if node.value > value:
            node.left = self.avl_add(node.left, value)
        elif node.value < value:
            node.right = self.avl_add(node.right, value)
        else:
            print("A Binary-Search Tree (BST) can't have nodes with repeated values. " +
                    "Repeated value: " + str(value))
            return node

        node.sub_tree_height = max(self.height(node.right), self.height(node.left)) + 1

        return self.balance(node, value)

    def balance(self, node, value):
        balance_factor = self.get_balance_factor(node)

        if balance_factor > 1:
            if node.right.value > value:
                right = node.right
                self.rotate_right(right)
            return self.rotate_left(node)

        elif balance_factor < -1:
            if node.left.value < value:
                left = node.left
                self.rotate_left(left)
            return self.rotate_right(node)

        return node

    def get_balance_factor(self, node):

        balance_factor = (-1) * self.height(node.left)
        balance_factor += self.height(node.right)

        return balance_factor

    def rotate_left(self, node):
        biggest_son = node.right
        node.right = biggest_son.left
        biggest_son.left = node

        node.sub_tree_height = max(self.height(node.left), self.height(node.right)) + 1
        biggest_son.sub_tree_height = max(self.height(biggest_son.left), self.height(biggest_son.right)) + 1
        print(biggest_son)
        print(biggest_son.left)
        print(node)

        return biggest_son

    def rotate_right(self, node):
        smallest_son = node.left
        node.left = smallest_son.right
        smallest_son.right = node

        node.sub_tree_height  = max(self.height(node.left), self.height(node.right)) + 1
        smallest_son.sub_tree_height = max(self.height(smallest_son.left), self.height(smallest_son.right)) + 1

        return smallest_son

    def height(self, node):
        if node:
            return node.sub_tree_height
        return 0

    def in_order_ls(self, node, ls = []):
        if node.left:
            ls = self.in_order_ls(node.left, ls)

        ls.append(str(node))

        if node.right:
            ls = self.in_order_ls(node.right, ls)

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
