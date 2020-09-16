"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
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


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None:
            self.tail = None
            return 0
        else:
            self.size = 1
            current_node = self.head
            while current_node.get_next() is not None:
                self.size += 1
                current_node = current_node.get_next()
            return self.size

    def enqueue(self, value):
        new_node = Node(value)
        value = new_node.get_value()
        if self.tail is None:
            self.head = self.tail = new_node
            return value
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            return value

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        else:
            value = self.head.get_value()
            exit_node = self.head
            self.head = exit_node.get_next()
            return value


"""
# Implemented using an array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()
"""