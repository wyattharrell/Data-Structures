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

from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # we're gonna go in
        # if the value < root's value
        if value < self.value:
            # go left
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left:
                # then self.left is a Node
                # now what?
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value
        else:
            # go right
            # how do we go right?
            # we have to check if there is another node on the right side
            if self.right:
                # then self.right is a Node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
        return self.value == target

        # if self.value == target:
        #     return True
        # elif target < self.value:
        #     if self.left is not None:
        #         current = self.left
        #     while current is not None:
        #         if current.value == target:
        #             return True
        #         elif current.left.value < target:
        #             current = current.left
        #         elif current.right.value > target:
        #             current = current.right
        # elif target > self.value:
        #     if self.right is not None:
        #         current = self.right
        #     while current is not None:
        #         if current.value == target:
        #             return True
        #         elif current.left.value < target:
        #             current = current.left
        #         elif current.right.value > target:
        #             current = current.right
        # return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while (current.right):
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

            # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()

        q.append(self)
        while len(q) > 0:
            current = q.popleft()
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


            # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        stack.append(self)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
