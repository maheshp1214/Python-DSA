"""Stack using extending Singly Linked List"""
from SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.item_count
        
#Driver code
s5=Stack()
s5.push(10)
s5.push(20)
s5.push(30)
print("Total elements are ",s5.size())
print("Top element is ",s5.peek())
s5.pop()
print("Total elements are ",s5.size())
print("Top element is ",s5.peek())