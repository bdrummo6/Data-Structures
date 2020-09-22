"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out(LIFO) order.

1. Implement the Stack class using an list as the underlying storage structure.
   Make sure the Stack tests pass. (Complete)

2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure. Make sure the Stack tests pass. (Complete)

3. What is the difference between using an list vs. a linked list when implementing a Stack?
"""

from node import Node

# Implemented using a linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    # Adds a new Node with the given value to the top(head) of a list
    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            new_node.set_next(None)
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # Removes the Node at the top(head) of a list
    def pop(self):
        if self.head is None:
            return None

        value = self.head.get_value()
        self.size -= 1
        if self.head.get_next() is None:
            self.head = None
            self.tail = None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()

        return value

"""
# Implemented using a list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

"""


