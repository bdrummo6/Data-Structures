"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out(LIFO) order.

1. Implement the Stack class using an list as the underlying storage structure.
   Make sure the Stack tests pass. (Complete)

2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure. Make sure the Stack tests pass. (Complete)

3. What is the difference between using a list vs. a linked list when implementing a Stack?
    - Implementing a Stack using a list allows you to use built-in functions to len(), append() and pop() to
      get the length, add a node and remove a node from the top of the Stack. Using a linked list you have to keep
      track of the length by incrementing or decrementing the length depending on whether you are adding or removing
      a node from the stack. When adding or removing a node using a linked list you have to keep track of the next
      reference of the next reference of the inserted or removed node.
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
        # create a new Node using the given value
        new_node = Node(value)
        # increment the stack size by 1
        self.size += 1

        # if stack is empty set the `head` and `tail` to the new node
        if not self.head:
            new_node.set_next(None)
            self.head = self.tail = new_node
        # if list is not empty then set the new node as the new `head`
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # Removes the Node at the top(head) of a list
    def pop(self):
        # if stack is empty return None
        if not self.head:
            return None
        # retrieve the value of the current stack `head`
        value = self.head.get_value()

        # if the stack only contains 1 node then set the `head` and `tail` to None
        if not self.head.get_next():
            self.head = self.tail = None
        # if the stack contains more than 1 node then set the second node in the stack as the new `head`
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()

        # decrement the stack size by 1
        self.size -= 1

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


