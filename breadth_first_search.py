from collections import deque

from binary_search_tree import plant_tree, BinarySearchTree, Node

"""
1. Create queue with nodes that need to be cheched
2. Take next node out of the queue
3. Check if it's the node we're looking for.
4.A. YES - Done
4.B. NO - Mark node as checked. Add it's adjancent nodes to the queue.
5. Go to step 2
6. If queue is empty, search failed.
"""


tree = plant_tree()


def bfs(tree: BinarySearchTree, value):
    nodes_queue = deque()
    nodes_queue.append(tree.root)

    while nodes_queue:
        current_node = nodes_queue.popleft()
        if current_node.value == value:
            return current_node

        if current_node.left:
            nodes_queue.append(current_node.left)
        if current_node.right:
            nodes_queue.append(current_node.right)


def bfs_recursive(queue: deque, value):
    """
    >>> initial_queue = deque(); initial_queue.append(tree.root)
    >>> bfs_recursive(initial_queue, 170)
    170
    >>> bfs_recursive(initial_queue, 1512)

    """
    if len(queue) == 0:
        return

    current_node = queue.popleft()
    if current_node.value == value:
        return current_node

    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)

    return bfs_recursive(queue, value)
