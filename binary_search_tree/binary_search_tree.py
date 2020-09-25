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
# imports for BFT and DFT print
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
        if value < self.value:
            # if there is no left child already here
            if self.left is None:
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it then set it to the left
                self.left = BSTNode(value)
            # otherwise call insert on the left node
            else:
                self.left.insert(value)
        # otherwise (the new nodes value is greater than or equal to the current node value)
        else:
            # if there is no right child already here
            if self.right is None:
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it then set it to the right
                self.right = BSTNode(value)
            # otherwise call insert on the right node
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
        if self.value == target:
            # return True
            return True
        # check if the target is less than the current nodes value
        if target < self.value:
            # if there is no left child already here
            if self.left is None:
                # return False
                return False
            # otherwise
            else:
                # return a call of contains on the left child passing in the target value
                return self.left.contains(target)
        # otherwise (the target is greater than the current nodes value)
        else:
            # if there is no right child already here
            if self.right is None:
                # return False
                return False
            # otherwise
            else:
                # return a call of contains on the right child passing in the target value
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty tree
        if self is None:
            # return None
            return None
        # ----------------------------------------------
        # recursive approach
        # check if there is no node to the right
        if self.right is None:
            # return the nodes value
            return self.value
        # return a call to get max on the right child
        return self.right.get_max()
        # -----------------------------------------------

        # -----------------------------------------------
        # iterative aproach

        # initialise the max value
        # max_v = self.value
        # # get a ref to the current node
        # current = self
        # # loop while there is still a current node
        # while current:
        # # if the current value is greater than the max value, update the max value
        #     if current.value > max_v:
        #         max_v = current.value
        # # move on to the next right node
        #     current = current.right
        # # return the max value
        # return max_v
        # -----------------------------------------------

    # Return the minimum value found in the tree
    def get_min(self):
        # check for an empty tree
        if self is None:
            # return None
            return None
        # ----------------------------------------------
        # recursive approach
        # check if there is no node to the right
        if self.left is None:
            # return the nodes value
            return self.value
        # return a call to get max on the right child
        return self.left.get_min()
        # -----------------------------------------------

    # Call the function `fn` on the value of each node (DFT full)
    def for_each(self, fn):
        # call the function passing in the current nodes value
        fn(self.value)
        # if there is a node to the right
        if self.right:
            # call the function on the right value
            self.right.for_each(fn)
        # if there is a node to the left
        if self.left:
            # call the function on the left node
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # base case
        # if there are no more nodes
        if not self.value:
            # return
            return
        # if there is a node to the left
        if self.left:
            # call in order print on the left
            self.left.in_order_print()
        # print the value of the current node (self.value)
        print(self.value)
        # if there is a node to the right
        if self.right:
            # call in order print on the right
            self.right.in_order_print()
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):  # use a queue
        # create a queue
        queue = Queue()
        # enqueue the first node (self)
        queue.enqueue(self)
        # while there is data on the queue
        while queue:
            # dequeu from queue on to current_node
            current = queue.dequeue()
            # print the current_node's value
            print(current.value)
            # if the current_node has a left child
            if current.left:
                # enqueue the left child
                queue.enqueue(current.left)
            # if the current_node has a right child
            if current.right:
                # enqueue the right child
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self): # use a stack
        # create a stack
        stack = Stack()
        # push the first node (self)
        stack.push(self)
        # while there is data on the stack
        while stack: # (we can start from left or right) 
            # pop from stack on to current_node
            current = stack.pop()
            # print the current_node's value
            print(current.value)
            # if the current_node has a left child
            if current.right: # if current.left:
                # push the left child
                stack.push(current.right) # stack.push(current.left)
            # if the current_node has a right child
            if current.left: # if current.right:
                # push the right child
                stack.push(current.left) # stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # base case
        # if there are no more nodes
        if not self.value:
            # return
            return
        # print the value of the current node (self.value) pre-order
        print(self.value)
        # if there is a node to the left
        if self.left:
            # call in order print on the left
            self.left.pre_order_dft()
        # if there is a node to the right
        if self.right:
            # call in order print on the right
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # base case
        # if there are no more nodes
        if not self.value:
            # return
            return
        # if there is a node to the left
        if self.left:
            # call in order print on the left
            self.left.post_order_dft()
        # if there is a node to the right
        if self.right:
            # call in order print on the right
            self.right.post_order_dft()
        # print the value of the current node (self.value) post order
        print(self.value)
"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.insert(4)
# print(bst.contains(7))
print(bst.bft_print())
print(bst.dft_print())
# print(bst.get_min())
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# # bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
