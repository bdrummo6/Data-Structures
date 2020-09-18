"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
            self.head.prev = None
            self.length += 1
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
            self.length += 1

        return value

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # check for empty list
        if not self.head:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = self.tail = None
            self.length -= 1
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = self.tail = new_node
            self.length += 1
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next

            curr_node.next = new_node
            self.tail = curr_node.next
            self.tail.next = None
            self.tail.prev = curr_node
            self.length += 1

        return value

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # check for empty list
        if self.length == 0:
            return None
        # check if there is only one node
        elif self.length == 1:
            value = self.tail.value
            self.head = self.tail = None
            self.length -= 1
        else:
            value = self.tail.value
            current_node = self.head

            while current_node.next:
                # keep looping
                current_node = current_node.next

            self.tail = current_node.prev
            self.tail.next = None
            self.length -= 1

        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length == 0:
            return None
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)

        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0:
            return None
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

        return value

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        value = node.value
        if self.length == 0:
            return None
        elif self.head.value == value:
            self.remove_from_head()
        else:
            curr_node = self.head
            prev_node = curr_node.prev
            while curr_node.next:
                if curr_node.value == value:
                    break
                prev_node = curr_node
                curr_node = curr_node.next

            # Check if node with value exist in the list
            if curr_node.value != value:
                return None
            elif not curr_node.next:
                self.remove_from_tail()
            else:
                prev_node.next = curr_node.next
                prev_node.prev = curr_node.prev
                self.length -= 1

        return value

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        max_value = self.head.value
        curr_node = self.head.next
        while curr_node:
            if max_value < curr_node.value:
                max_value = curr_node.value
            curr_node = curr_node.next

        return max_value

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next