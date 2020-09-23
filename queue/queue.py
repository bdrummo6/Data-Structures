"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out(FIFO) order.

1. Implement the Queue class using an list as the underlying storage structure.
   Make sure the Queue tests pass. (Complete)

2. Re-implement the Queue class, this time using the linked list implementation as the underlying storage structure.
   Make sure the Queue tests pass.  (Complete)

3. What is the difference between using an list vs. a linked list when implementing a Queue?
    - Implementing a Queue using a list allows you to use built-in functions to len(), insert() and pop() to
      get the length, add a node and remove a node from a Queue. Using a linked list you have to keep
      track of the length by incrementing or decrementing the length depending on whether you are adding or removing
      a node from a Queue. When adding or removing a node using a linked list you have to keep track of the next
      reference of the inserted or removed node.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import *

# Queue implemented using a Singly Linked List
class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    # Adds a Node with the given value to the end of the Queue(linked list)
    def enqueue(self, value):
        # call the add_to_tail function to add an item to the end of a Queue
        self.add_to_tail(value)

    # Removes a Node from the front of the Queue(Linked list)
    def dequeue(self):
        # call the remove_head function to remove the first node in a Queue
        value = self.remove_head()

        return value

    def print_queue(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.get_value())
            curr_node = curr_node.get_next()


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

q = Queue()

q.enqueue(15)
q.enqueue(17)
q.enqueue(25)
q.dequeue()
q.enqueue(36)
q.enqueue(17)
q.dequeue()

print()
q.print_queue()  # 25 36 17

print()
print(len(q))  # 3
