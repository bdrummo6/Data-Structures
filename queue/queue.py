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

from node import Node

# Queue implemented using a Singly Linked List
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    # Adds a Node with the given value to the end of the Queue(linked list)
    def enqueue(self, value):
        # create a new node using the given value
        new_node = Node(value)
        # increment the queue's size by 1
        self.size += 1

        # if the queue is empty then set the `head` and `tail` to the new node
        if not self.tail:
            self.head = self.tail = new_node
        # if the queue is not empty then set the new node as the new `tail`
        else:
            # set the next reference of the current `tail` to the new node
            self.tail.set_next(new_node)
            # set the `tail` reference to the new node
            self.tail = new_node

    # Removes a Node from the front of the Queue(Linked list)
    def dequeue(self):
        # if the list is empty return None
        if not self.head:
            return None

        # retrieve the `head` node's value
        value = self.head.get_value()

        # if the queue contains only 1 node then set the `head` and `tail` to None
        if not self.head.get_next():
            self.head = self.tail = None
        # if the queue contains more then 1 node then set the second node as the new `head`
        else:
            node = self.head
            self.head = node.get_next()

        # decrement the size of the queue by 1
        self.size -= 1

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
