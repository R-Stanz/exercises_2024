from complete_binary_tree import CompleteBinaryTree

tree = CompleteBinaryTree()
tree.add(1)
tree.add(3)
tree.add(4)
tree.add(2)
tree.add(-2)
tree.add(1)

print(tree)
print("The Tree Minimun Value Is: {}".format(tree.min_value()))
print("The Tree Maximum Value Is: {}".format(tree.max_value()))
