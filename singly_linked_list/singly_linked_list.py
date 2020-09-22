
# Node class
# Instances of Node contain a value and a pointer(reference) to the next Node in a list or None if at the end of a list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# (Singly) Linked List Class
# Instances contain references to the head(start) and tail(end) of a list, plus size which holds the amount of Nodes
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Returns the number of Nodes in a list
    def __len__(self):
        return self.size

    # Adds a Node with the given value at the end of a list
    def add_to_tail(self, value):
        new_node = Node(value)
        self.size += 1
        # checks if the linked list is empty
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # Removes the Node at the end of the list
    def remove_tail(self):
        # check for empty list and returns None if it is
        if self.head is None:
            return None

        self.size -= 1
        value = self.tail.get_value()
        # check if there is only one node and sets both the head and tail to None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()

            self.tail = current_node
            self.tail.set_next(None)

        return value

    # Removes the first Node in a list
    def remove_head(self):
        # check for empty list and returns None if it is
        if self.head is None:
            return None

        self.size -= 1
        value = self.head.get_value()

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.get_next()

        return value

"""
ll = LinkedList()

print(len(ll))  # 0
ll.add_to_tail(14)
print(ll.head.get_value())  # 14
print(ll.tail.get_value())  # 14
print(len(ll))  # 1
ll.add_to_tail(56)
print(ll.head.get_value())  # 14
print(ll.tail.get_value())  # 56
print(len(ll))  # 2
ll.add_to_tail(35)
print(ll.head.get_value())  # 14
print(ll.tail.get_value())  # 35
print(len(ll))  # 3
ll.add_to_tail(76)
print(ll.head.get_value())  # 14
print(ll.tail.get_value())  # 76
print(len(ll))  # 4

print()
ll.remove_tail()
print(ll.head.get_value())  # 14
print(ll.tail.get_value())  # 35
print(len(ll))  # 3
ll.remove_head()
print(ll.head.get_value())  # 56
print(ll.tail.get_value())  # 35
print(len(ll))  # 2
"""