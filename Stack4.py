"""Stack using import Singly Linked List"""
from SLL import *

class Stack:
    def __init__(self):
        self.mylist=SLL() #creating ,SLL as object of stack class
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    def size(self):
        return self.item_count
        
#driver code
s4=Stack()
s4.push(10)
s4.push(20)
s4.push(30)
print("Total elements are ",s4.size())
print("Top elemetn is ",s4.peek())
s4.pop()
print("Total elements are ",s4.size())
print("Top elemetn is ",s4.peek())
    