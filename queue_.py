from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: Node | None = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value=value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return

        if self.first == self.last:
            self.last = None

        to_deque = self.first
        self.first = self.first.next
        self.length -= 1
        return to_deque.value

    def peek(self):
        return self.first
