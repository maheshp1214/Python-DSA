"""Stack using List"""
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
            
    
#Driver code    
s1=Stack()
print(s1.is_empty())
# print(s1.peek())
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
print("The top element is ",s1.peek())
print("Removed element is ",s1.pop())
print("Now,The top element is ",s1.peek())
print("Total elements in this stack is ",s1.size())