"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# Implemented using a linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None and self.tail is None:
            return 0
        else:
            self.size = 1
            current_node = self.head
            while current_node.get_next() is not None:
                self.size += 1
                current_node = current_node.get_next()
            return self.size

    def push(self, value):
        new_node = Node(value)
        value = new_node.get_value()
        if self.head is None:
            self.head = new_node
            return value
        else:
            new_node.set_next(self.head)
            self.head = new_node
            return value

    def pop(self):
        if self.head is None:
            return None
        else:
            pop_node = self.head
            value = pop_node.get_value()
            self.head = self.head.get_next()
            pop_node.set_next(None)
            return value



"""
# Implemented using an array
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