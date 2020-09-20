
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

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        self.size = 0

        curr_node = self.head
        while curr_node:
            self.size += 1
            curr_node = curr_node.get_next()

        return self.size

    def add_to_tail(self, value):
        new_node = Node(value)
        # checks if the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

        return value

    def remove_tail(self):
        # check for empty list
        if self.head is None:
            return None
        # check if there is only one node
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
        else:
            value = self.tail.get_value()

            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()

            self.tail = current_node
            self.tail.set_next(None)

        return value

    def remove_head(self):
        # check for empty list
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            value = self.head.get_value()
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