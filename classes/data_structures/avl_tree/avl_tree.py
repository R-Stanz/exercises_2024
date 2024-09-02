from node import Node
from copy import deepcopy

class Avl_tree:
    root = None
    def __init__ (self):
        pass

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            last_visited = self.avl_add(self.root, value, height=1)

    def avl_add(self, node, value, height):
        if not node:
            return Node(value, height)

        left = node.left
        right = node.right
        if (left and left.value == value) or (right and right.value == value):
            print("A Binary-Search Tree (BST) can't have nodes with repeated values\n" +
                    "Repeated value: " + str(value))
            return node

        if node.value > value:
            node.left = self.avl_add(left, value, height+1)

        if node.value < value:
            node.right = self.avl_add(right, value, height+1)

        return node#return self.balance(node, value)

    def balance(self, node, value):
        balance_factor = self.get_balance_factor(node)

        #left = self.rotate_left(node)
        '''
        if balance_factor > 1:
            if node.right.value > value:
                right = node.right
                right = rotate_right(right)
                return rotate_left(node)
            else:
                return rotate_left(node)

        elif balance_factor < -1:
            if node.left.value > value:
                left = node.left
                left = rotate_left(left)
                return rotate_right(node)
            else:
                return rotate_right(node)
        '''

        return node

    def get_balance_factor(self, node):
        balance_factor = 0

        right = node.right
        if right:
            balance_factor += right.value

        left = node.left
        if left:
            balance_factor -= left.value

        return balance_factor

    def rotate_left(self, node):
        biggest_son = deepcopy(node.right)

        #node.right = biggest_son.left
        #biggest_son.left = node
        #update_heights(node)
    
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
