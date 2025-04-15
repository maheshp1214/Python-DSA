"""Stack using Extending List"""
class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop() #super() function explicitly calls parent's class function if we use self.pop(),which creates recursion or method overriding
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise ImportError("Stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data): #way of restrict 'insert' method
        raise AttributeError("No Attribute 'insert' in stack")

s2=Stack()
s2.push(4)
s2.push(5)
s2.push(6)
print("Top value is ",s2.peek())
print("Length of stack is ",s2.size())
print("Deleted value is ",s2.pop())


