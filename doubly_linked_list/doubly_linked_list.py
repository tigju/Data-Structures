"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

            
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
        # instantiate a new node
        new_node = ListNode(value)
        #if self.head is None
        if self.head is None and self.tail is None:
            # set head's previous to None
            new_node.prev = None
            # set new node as head
            self.head = new_node 
            self.tail = new_node
            # update length
            self.length += 1
        # if self.head is not None
        else:
            # set new_node as current head's previous node 
            self.head.prev = new_node
            # set current head as next for new_node
            new_node.next = self.head
            # set new new_node as new head
            self.head = new_node
            # set new head's previous as None
            new_node.prev = None
            # update tail
            curr = self.head
            while curr.next:
                curr = curr.next
            self.tail = curr
            # update length
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        current = self.head.value
        self.delete(self.head)
        return current
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # instantiate a new node
        new_node = ListNode(value)
        # if there is no head and no tail
        if self.head is None and self.tail is None:
            # assign new node to head and tail
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new_node as the current tail's next
            self.tail.next = new_node
            # set the current tail as previous node of the new node
            new_node.prev = self.tail
            # set the new node as a new tail
            self.tail = new_node
            # update length
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current = self.tail.value
        self.delete(self.tail)
        return current    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if the node passed is a tail of the list
        if node == self.tail:
            # set prev tail's value as a new tail 
            self.tail = self.tail.prev
            # set new tail's next value to None
            self.tail.next = None
        # set old tail's node as a prev of current head
        self.head.prev = node
        # set current head as a next node of this node
        node.next = self.head
        # set this node as a new head 
        self.head = node
        # set head prev to None
        self.head.prev = None

        #DRY
        # if node is self.head:
        #     return
        # value = node.value
        # if node is self.tail:
        #     self.remove_from_tail()
        # else:
        #     node.delete()

        #     self.length -= 1
        # self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if the node passed is a head of the list
        if node == self.head:
            # set next head's value as a new head
            self.head = self.head.next
            # set new tail's prev value to None
            self.head.prev = None
        # set old tail's node as a prev of current head
        self.tail.next = node
        # set current head as a next node of this node
        node.prev = self.tail
        # set this node as a new head
        self.tail = node
        # set head prev to None
        self.tail.next = None

        #DRY code 
        # if node is self.tail:
        #     return
        # value = node.value
        # if node is self.head:
        #     self.remove_from_head()
        # else:
        #     node.delete()

        #     self.length -= 1
        # self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # base case if head 
        if self.head is None:
            # return None
            return None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            node.delete()
        else:
            node.delete()
        self.length -= 1
            




    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # set max and current starting point (head)
        max = current = self.head
        # while current is not None iterate
        while current:
            # if max value less then current value
            if max.value < current.value:
                # set current value to max value variable
                max.value = current.value
            # update current to next
            current = current.next
        # return max value in a list
        return max.value
        

dll = DoublyLinkedList()
dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_head(3)
dll.add_to_head(4)
# print(dll.head.value)
dll.add_to_head(5)
# print(dll.head.value)


# print("head, prev and next")
# print(dll.head.value)
# print(dll.head.prev)
# print(dll.head.next.value)
# print("tail, prev and next")
# print(dll.tail.value)
# print(dll.tail.prev.value)
# print(dll.tail.next)
# dll.move_to_front(dll.tail.prev)
# print("new head, prev and next")
# print(dll.head.value)
# print(dll.head.prev)
# print(dll.head.next.value)
dll.delete(dll.head.next)
print(dll.head.next.prev.value)

