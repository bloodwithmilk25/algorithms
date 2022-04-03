from __future__ import annotations

from copy import copy
from dataclasses import dataclass
from typing import Any, List


@dataclass
class Node:
    value: Any
    next: Node | None = None
    prev: Node | None = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList:
    def __init__(self, values: List[Any] = None):
        self.length = 0
        if not values:
            return

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
            new_node.prev = prev_node
            prev_node = new_node
            self.length += 1

        self.tail = prev_node

    def append(self, value):
        new_node = self._create_node(value, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = self._create_node(value, self.head)
        self.head.prev = new_node
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
                new_node = self._create_node(value, next_node, prev=node)
                next_node.prev = new_node
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
                if node.next:
                    node.next.prev = node

                if node.next is None:
                    self.tail = node

                self.length -= 1
                return

    def reverse(self) -> DoublyLinkedList:
        if self.length == 0:
            return DoublyLinkedList()

        reversed_ll = DoublyLinkedList()
        for i, node in enumerate(reversed(self)):
            new_node = copy(node)
            new_node.next = None
            new_node.prev = None

            if i == 0:
                reversed_ll.head = new_node
                reversed_ll.tail = new_node
                reversed_ll.length += 1
                continue

            reversed_ll.append(node.value)

        return reversed_ll

    @staticmethod
    def _create_node(value, next_: Node | None = None, prev: Node | None = None):
        return Node(value=value, next=next_, prev=prev)

    def __str__(self):
        return f'Length: {self.length}; {"->".join(n.value for n in self)}'

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __reversed__(self):
        current_node = self.tail
        while current_node:
            yield current_node
            current_node = current_node.prev
