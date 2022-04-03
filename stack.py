from __future__ import annotations
from dataclasses import dataclass
from typing import Any


class Stack:
    def __init__(self):
        self.length = 0
        self._storage = list()

    def peek(self):
        return self._storage[-1]

    def pop(self):
        self.length -= 1
        return self._storage.pop()

    def push(self, value):
        self._storage.append(value)
        self.length += 1


# Now let's implement Stack on top of Linked list

@dataclass
class Node:
    value: Any
    next: Node | None = None


class StackLL:
    def __init__(self):
        self.top: Node = None
        self.bottom: Node = None
        self.length = 0

    def push(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return

        popped_node = self.top
        self.top = self.top.next
        self.length -= 1

        if popped_node == self.bottom:
            self.bottom = None

        return popped_node.value

    def peek(self):
        return self.top.value
