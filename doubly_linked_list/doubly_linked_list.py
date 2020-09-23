
"""
Each ListNode holds a reference to its previous node as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    # deletes a node by removing next and previous references to it from the nodes before it and after it in a list
    def delete(self):
        # Sets the current node's previous node's next reference to the current node's next reference
        if self.prev:
            self.prev.set_next(self.get_next())
        # Sets the current node's next node's previous reference to the current node's previous reference
        if self.next:
            self.next.set_prev(self.get_prev())

"""
Our doubly-linked list class. It holds references to the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node using the given value
        new_node = ListNode(value)
        # increment the length
        self.length += 1
        # check if the linked list is empty
        if not self.head and not self.tail:
            # Set both `head` and `tail` to the new node
            self.head = self.tail = new_node
        # Otherwise just add the new node to the `head`
        else:
            # set the new node's `next` reference to the `head` of the list
            new_node.set_next(self.head)
            # set the head's `prev` reference to the new node
            self.head.set_prev(new_node)
            # set the list's `head` reference to the new node
            self.head = new_node

    """
    Removes the List's current head node, making the current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # retrieve the value in the `head` node
        value = self.head.value
        # call the delete function on the `head` node
        self.delete(self.head)

        return value

    """
    Wraps the given value in a ListNode and inserts it as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create a new_node to insert using the given value
        new_node = ListNode(value)
        # Increment the list's length by 1
        self.length += 1
        # if the list is empty then set the references of the `head` and `tail` to the new node
        if not self.tail and not self.head:
            self.tail = self.head = new_node
        # if list is not empty then just add the new node to the list's `tail`
        else:
            # set the prev node reference of the new node to the list's `tail`
            new_node.set_prev(self.tail)
            # set the `tail` next node reference to the new node
            self.tail.set_next(new_node)
            # set the list's `tail` reference to the new node
            self.tail = new_node

    """
    Removes the List's current tail node, making the current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # retrieve the value in the `tail` node
        value = self.tail.value
        # call the delete function on the `tail` node
        self.delete(self.tail)

        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if the node is already at the front
        if node is self.head:
            return None
        # retrieve the value of the given node
        value = node.value
        # call the delete function on the given node
        self.delete(node)
        # add the node with the given value to the front of the list
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if the node is already at the end
        if node is self.tail:
            return None
        # retrieve the value of the given node
        value = node.value
        # call the delete function on the given node
        self.delete(node)
        # add the node with the given value to the end of the list
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the order of the other elements of the List.
    """
    def delete(self, node):
        # retrieve the value of the given node
        value = node.value
        # if the list is empty
        if not self.head and not self.tail:
            return None
        # if the list only contains one node and if so then set the `head` and `tail` to None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if the given node is the `head` node
        elif self.head is node:
            self.head = node.get_next()
            node.delete()  # call the ListNode's delete function on the given node
        # if the given node is the list's `tail` node
        elif self.tail is node:
            self.tail = node.get_prev()
            node.delete()  # call the ListNode's delete function on the given node
        else:
            node.delete()  # call the ListNode's delete function on the given node

        # decrement the list's length by 1
        self.length -= 1

        return value

    """
    Finds and returns the maximum value of all the nodes in the List.
    """
    def get_max(self):
        # check if the list is empty
        if not self.head and not self.tail:
            return None
        # set's the initial max value to the `head` node's value
        max_value = self.head.get_value()
        # set the reference of `head` to a curr_node to iterate through the list
        curr_node = self.head
        # will loop through each node's value in the list
        while curr_node:
            # checks the curr_node value against the current max value
            if curr_node.get_value() > max_value:
                # if the curr_node value is greater than the max value the it becomes the new max value
                max_value = curr_node.get_value()
            # sets the next node's reference to the curr_node to move to the next node
            curr_node = curr_node.get_next()

        return max_value

