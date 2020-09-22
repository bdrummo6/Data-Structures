"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

"""
Our doubly-linked list class. It holds references to the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        self.length = 0
        curr_node = self.head
        while curr_node is not None:
            self.length += 1
            curr_node = curr_node.get_next()

        return self.length

    """
    Wraps the given value in a ListNode and inserts it as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.set_prev(None)
        else:
            new_node.set_next(self.head)
            new_node.set_prev(None)
            self.head = new_node

        return value

    """
    Removes the List's current head node, making the current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.get_value()
        # check for empty list
        if self.head is None:
            return None
        elif self.head.get_next() is None:
            self.head = self.tail = None
        else:
            self.head = self.head.get_next()
            self.head.set_prev(None)

        return value

    """
    Wraps the given value in a ListNode and inserts it as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            curr_node = self.head
            while curr_node.get_next() is not None:
                curr_node = curr_node.get_next()

            curr_node.set_next(new_node)
            self.tail = curr_node.get_next()
            self.tail.set_next(None)
            self.tail.set_prev(curr_node)

        return value

    """
    Removes the List's current tail node, making the current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # check for empty list
        if self.head is None:
            return None
        # check if there is only one node
        elif self.head.get_next() is None:
            value = self.tail.get_value()
            self.head = self.tail = None
        else:
            value = self.tail.get_value()
            current_node = self.head

            while current_node.get_next() is not None:
                # keep looping
                current_node = current_node.get_next()

            self.tail = current_node.get_prev()
            self.tail.set_next(None)

        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None:
            return None
        else:
            value = node.get_value()
            self.delete(node)
            self.add_to_head(value)

        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None:
            return None
        else:
            value = node.get_value()
            self.delete(node)
            self.add_to_tail(value)

        return value

    """
    Deletes the input node from the List, preserving the order of the other elements of the List.
    """
    def delete(self, node):
        value = node.get_value()
        if self.head is None:
            return None
        elif self.head.get_value() == value:
            self.remove_from_head()
        else:
            curr_node = self.head
            prev_node = curr_node.get_prev()
            while curr_node.get_next() is not None:
                if curr_node.get_value() == value:
                    break
                prev_node = curr_node
                curr_node = curr_node.get_next()

            # Check if node with value exist in the list
            if curr_node.get_value() != value:
                return None
            elif curr_node.get_next() is None:
                self.remove_from_tail()
            else:
                prev_node.set_next(curr_node.get_next())
                prev_node.set_prev(curr_node.get_prev())

        return value

    """
    Finds and returns the maximum value of all the nodes in the List.
    """
    def get_max(self):
        max_value = self.head.get_value()
        curr_node = self.head.get_next()
        while curr_node is not None:
            if max_value < curr_node.get_value():
                max_value = curr_node.get_value()
            curr_node = curr_node.get_next()

        return max_value

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.get_value())
            curr_node = curr_node.get_next()


dll = DoublyLinkedList()

# add_to_head
dll.add_to_head(7)  # 7
dll.add_to_head(12)  # 12 7
dll.add_to_head(23)  # 23 12 7
dll.add_to_head(35)  # 35 23 12 7
dll.add_to_head(54)  # 54 35 23 12 7

# remove_from_head
dll.remove_from_head()  # 35 23 12 7

# add_to_tail
dll.add_to_tail(16)  # 35 23 12 7 16
dll.add_to_tail(45)  # 35 23 12 7 16 45
dll.add_to_tail(76)  # 35 23 12 7 16 45 76

dll.print_list()
print()
# remove_from_tail
dll.remove_from_tail()  # 35 23 12 7 16 45

# move_to_front
dll.move_to_front(ListNode(16))  # 16 35 23 12 7 45

# move_to_back
dll.move_to_end(ListNode(23))  # 16 35 12 7 45 23

# delete
dll.delete(ListNode(12))  # 16 35 7 45 23

dll.print_list()  # 16 35 7 45 23

# list max value
print('\nMax value: ' + str(dll.get_max()))  # 45

# list length
print('\nList Length: ' + str(len(dll)))  # 5
