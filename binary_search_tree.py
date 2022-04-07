class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class BinarySearchTree():
    def __init__(self):
        self.root: Node = None

    def insert(self, value: int):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if value >= current_node.value:
                if not current_node.right:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            else:
                if not current_node.left:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left

    def lookup(self, value):
        current_node = self.root

        while current_node:
            if current_node.value == value:
                return current_node
            if current_node.value < value:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return

    def remove(self, value):
        current_node = self.root
        prev_node = None

        while current_node:
            if current_node.value == value:

                if current_node.right is None:
                    if prev_node is None:
                        self.root = current_node.left
                    else:
                        if current_node.value < prev_node.value:
                            prev_node.left = current_node.left
                        else:
                            prev_node.right = current_node.left

                elif current_node.right.left is None:
                    if prev_node is None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left
                        if current_node.value < prev_node.value:
                            prev_node.left = current_node.right
                        else:
                            prev_node.right = current_node.right
                else:
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left

                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if prev_node is None:
                        self.root = left_most
                    else:
                        if current_node.value < prev_node.value:
                            prev_node.left = left_most
                        else:
                            prev_node.right = left_most
                return

            # just looping further
            elif current_node.value < value:
                prev_node = current_node
                current_node = current_node.right
            else:
                prev_node = current_node
                current_node = current_node.left


# Insert elements
def plant_tree() -> BinarySearchTree:
    """
          9
      4     20
    1  6  15  170
    """
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    return tree


def printTree(node: Node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 6 * level + '-> ' + str(node.value))
        printTree(node.left, level + 1)
