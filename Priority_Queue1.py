"""Priority Queue using List"""
class PriorityQueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data,priority): #prioroty is for priority number.
        index=0 #initially list index is zero,lower no. higher priority.
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            return self.items.pop(0)[0] #pop(0) returns tuple(data,priority),but pop(0)[0] return data only.
    def size(self):
        return len(self.items)
    
p1=PriorityQueue()
p1.push("Punit",3)
p1.push("Harsh",1)
p1.push("Mahesh",8)
p1.push("Jay",4)
print("No of elements are = ",p1.size())

while not p1.is_empty():
    print(p1.pop())

print(p1.is_empty())

                