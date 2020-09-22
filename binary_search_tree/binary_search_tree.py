"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare the new value with the parent node
        if self.value:
            # if value is less than the current parent node value
            if value < self.value:
                # if there is no left child node then a new node with the value is inserted to the left
                if self.left is None:
                    self.left = BSTNode(value)
                # if there is a left child node then insert is called on the left child node
                else:
                    self.left.insert(value)
            # if value is greater than or equal to the current parent node value
            elif value >= self.value:
                # if there is no right child node then a new node with the value is inserted to the right
                if self.right is None:
                    self.right = BSTNode(value)
                # if there is a right child node then insert is called on the right child node
                else:
                    self.right.insert(value)
        # if the root node of the BST is None then the new value is assigned to the root node's value
        else:
            self.value = value

    # Return True if the tree contains the value and False if it does not
    def contains(self, target):
        if not self:
            return False
        # if the target value is less than current parent node's value
        if target < self.value:
            # if there is no left child node then the BST does not contain the target value
            if not self.left:
                return False
            # if there is a left child node then contains is called on the left child node
            return self.left.contains(target)
        # if the target value is greater than or equal to the current parent node's value
        elif target > self.value:
            # if there is no right child node then the BST does not contain the target value
            if not self.right:
                return False
            # if there is a right child node then contains is called on the right child node
            return self.right.contains(target)
        # target value is equal to the current node value
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # checks if the BST is empty
        if not self:
            return None

        curr_node = self
        # loop down to find the rightmost leaf which will hold the maximum value
        while curr_node.right:
            curr_node = curr_node.right

        return curr_node.value

    """        
        # Recursive method for get_max()
        if not self:
            return None

        if not self.right:
            return self.value

        return self.right.get_max()
    """

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # checks if the current node is None
        if not self:
            return None
        # if there is a left child node of the current parent node then call for_each on the left child node
        if self.left:
            self.left.for_each(fn)
        fn(self.value)  # call the callback function fn on the current node's value
        # if there is a right child node of the current parent node then call for_each on the right child node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # checks if the current node is None
        if self is None:
            return None
        # if there is a left child node of the current parent node then call in_order_print on the left child node
        if self.left:
            self.left.in_order_print()
        print(self.value) # prints current node's value
        # if there is a right child node of the current parent node then call in_order_print on the right child node
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node, in an iterative breadth first traversal
    def bft_print(self):
        # using a Queue for this function
        bst_q = Queue()

        # Insert the root node into the queue
        bst_q.enqueue(self)

        # loops while the queue length is greater than 0
        while len(bst_q) > 0:
            # removes front node and stores it into curr_node
            curr_node = bst_q.dequeue()
            print(curr_node.value)  # prints the curr_node value
            # if there is a left child node then insert the left child node at the rear of the queue
            if curr_node.left:
                bst_q.enqueue(curr_node.left)
            # if there is a right child node then insert the right child node at the rear of the queue
            if curr_node.right:
                bst_q.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node, in an iterative depth first traversal
    def dft_print(self):
        # using a Stack for this function
        bst_s = Stack()

        bst_s.push(self)

        while len(bst_s) > 0:
            curr_node = bst_s.pop()
            print(curr_node.value)
            if curr_node.left:
                bst_s.push(curr_node.left)
            if curr_node.right:
                bst_s.push(curr_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self is None:
            return None

        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self is None:
            return None

        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
# initialization
bst = BSTNode(1)

# insert
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# in_order_print function
print('\nUsing in_order_print function to print node values from lowest to highest: ')
bst.in_order_print()  # 1 2 3 4 5 6 7 8

# contains function
print('\nContains 7: ' + str(bst.contains(7)))  # True
print('Contains 1: ' + str(bst.contains(1)))  # True
print('Contains 11: ' + str(bst.contains(11)))  # False

# get_max function
print('\nMax Value: ' + str(bst.get_max()))  # 8

# test function for for_each function
def print_add_5(val):
    sum1 = val + 5
    print(sum1)

# for_each function
print('\nUsing for_each function to add 5 to each node value: ')
bst.for_each(print_add_5)  # 6 7 8 9 10 11 12 13

# bft_print
print('\nBreadth first traversal:')
bst.bft_print()

# dft_print
print('\nDepth first traversal:')
bst.dft_print()

# pre_order_dft
print("\nPre-order DFT:")
bst.pre_order_dft()

# post_order_dft
print("\nPost-order DFT:")
bst.post_order_dft()

"""
print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
"""