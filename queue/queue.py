"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

### 1. Implementation using array structure
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)
#         return self.storage

#     def dequeue(self):
#         if self.__len__() > 0:
#             x = self.storage.pop(0)
#             return x
#         else:
#             return None

### 2. Implementation using Linked list

from singly_linked_list import LinkedList


class Queue(LinkedList):
    
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.get_next()
        return count

    def enqueue(self, value):
        # use inherited add_to_tail() of a LinkedList class
        return super().add_to_tail(value)
        
    def dequeue(self):
        # use inherited remove_head() of a LinkedList class
        return super().remove_head()



## 3. What is the difference between using an array vs. a linked list when implementing a Queue?
'''
Both arrays and linked lists used to store linear data, however
with a linked list would work faster when manipulating data in the middle of 
the queue for example add or delete - O(1). 
Array in other hand, requires more memory, it would be O(n) because you have to move 
other elements to create the space for the new element, 
or fill the space of the deleted element.
'''
