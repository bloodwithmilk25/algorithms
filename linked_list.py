from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: Node | None = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self, *values: Any):
        self.length = 0
        if len(values) == 1:
            node = Node(values[0])
            self.head = node
            self.tail = node
            self.length = 1
            return

        prev_node = None
        for i, value in enumerate(values):
            new_node = self._create_node(value)
            if i == 0:
                self.head = new_node
                prev_node = self.head
                self.length += 1
                continue

            prev_node.next = new_node
            prev_node = new_node
            self.length += 1

        self.tail = prev_node

    def append(self, value):
        new_node = self._create_node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = self._create_node(value, self.head)
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)

        for i, node in enumerate(self):
            if i == index - 1:
                next_node = node.next
                new_node = self._create_node(value, next_node)
                node.next = new_node
                self.length += 1
                return

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        if index >= self.length:
            return

        for i, node in enumerate(self):
            if i == index - 1:
                next_node = node.next
                node.next = next_node.next if next_node else None
                if node.next is None:
                    self.tail = node

                self.length -= 1
                return

    @staticmethod
    def _create_node(value, next_: Node | None = None):
        return Node(value=value, next=next_)

    def __str__(self):
        return f'Length: {self.length}; {"->".join(n.value for n in self)}'

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
