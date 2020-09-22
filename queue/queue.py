"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out(FIFO) order.

1. Implement the Queue class using an list as the underlying storage structure.
   Make sure the Queue tests pass. (Complete)

2. Re-implement the Queue class, this time using the linked list implementation as the underlying storage structure.
   Make sure the Queue tests pass.  (Complete)

3. What is the difference between using an list vs. a linked list when implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from node import Node

# Queue implemented using a Singly Linked List
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        self.size = 0

        curr_node = self.head

        # Loop while end of queue is not reached
        while curr_node:
            self.size += 1
            curr_node = curr_node.get_next()

        return self.size

    # Adds a Node with the given value to the end of the Queue(linked list)
    def enqueue(self, value):
        new_node = Node(value)
        value = new_node.get_value()
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

        return value

    # Removes a Node from the front of the Queue(Linked list)
    def dequeue(self):
        if self.head is None:
            return None
        elif self.head.get_next() is None:
            value = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            value = self.head.get_value()
            exit_node = self.head
            self.head = exit_node.get_next()

        return value


"""
# Implemented using a list
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
