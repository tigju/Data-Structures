"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

### 1. implementation using arrays
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         return self.storage

#     def pop(self):
#         if self.__len__() > 0:
#             x = self.storage.pop()
#             return x
#         else:
#             return None

## 2. Re-implement using LinkedList class
from singly_linked_list import LinkedList, Node


class Stack(LinkedList, Node):
        def __init__(self):
            self.head = None
            self.tail = None

        def __str__(self):
            temp = self.head
            stk = []
            while temp:
                stk.append(temp)
                temp = temp.get_next()
            return f"{[v.get_value() for v in stk]}"

        def __len__(self):
            temp = self.head
            count = 0
            while temp:
                count += 1
                temp = temp.get_next()
            return count

        def push(self, value):
            # use inherited add_to_tail() of a LinkedList class
            return super().add_to_tail(value)

        def pop(self):
            # use inherited remove_tail() from LinkedList class
            return super().remove_tail()
        
        def peek(self):
            return f"{self.tail.get_value()}"


stack1 = Stack()
stack1.push(10)
stack1.push(15)
print(stack1.head)
print(len(stack1))
print(stack1.peek())
print(stack1)
