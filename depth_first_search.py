from queue import LifoQueue

from binary_search_tree import plant_tree, BinarySearchTree, Node

tree = plant_tree()


def dfs(tree: BinarySearchTree, value):
    """
    preorder dfs
    """
    nodes_stack = LifoQueue()
    nodes_stack.put(tree.root)
    while not nodes_stack.empty():
        current_node = nodes_stack.get()
        print(current_node.value)
        if current_node.value == value:
            return value

        if current_node.right:
            nodes_stack.put(current_node.right)
        if current_node.left:
            nodes_stack.put(current_node.left)
