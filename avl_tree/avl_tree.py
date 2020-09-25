"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node:
            print('-' * level * 2, pref, self.node.key, f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left:
                self.node.left.display(level + 1, '<')
            if self.node.right:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        # checks if the current node is None
        if not self.node:
            self.height = -1
        elif self.node and not self.node.left and not self.node.right:
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            self.height += 1
        else:
            if self.node.left:
                self.node.left.update_height()
            if self.node.right:
                self.node.right.update_height()

            self.height = 1 + max(self.node.left.height, self.node.right.height)

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if not self.node:
            self.balance = 0
        elif self.node and not self.node.left and not self.node.right:
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        else:
            if self.node.left:
                self.node.left.update_balance()
            if self.node.right:
                self.node.right.update_balance()

            self.balance = self.node.left.height - self.node.right.height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent.
    """
    def left_rotate(self):
        # Rotate left pivoting on self
        a = self.node
        b = self.node.right.node
        t = b.left.node

        self.node = b
        b.left.node = a
        a.right.node = t

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent.
    """
    def right_rotate(self):
        # Rotate right pivoting on self
        a = self.node
        b = self.node.left.node
        t = b.right.node

        self.node = b
        b.right.node = a
        a.left.node = t

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height()
        self.update_balance()
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                self.right_rotate()
                self.update_height()
                self.update_balance()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()
                self.left_rotate()
                self.update_height()
                self.update_balance()

    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if not self.node:
            self.node = Node(key)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key:
            self.node.left.insert(key)
            self.update_height()
        elif key >= self.node.key:
            self.node.right.insert(key)

        self.rebalance()

    # Prints node keys from lowest to highest
    def in_order_print(self):
        # checks if the current node is None
        if not self.node:
            return None
        elif self.node and not self.node.left and not self.node.right:
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        else:
            if self.node.left:
                self.node.left.in_order_print()
            print(self.node.key)
            if self.node.right:
                self.node.right.in_order_print()



