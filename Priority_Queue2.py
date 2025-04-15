"""Priority Queue using Linked List"""
class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priority):
        n=Node(data,priority)
        if self.is_empty() or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next!=None and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
    def size(self):
        return self.item_count
    
#Driver code
p2=PriorityQueue()
p2.push("Punit",3)
p2.push("Harsh",1)
p2.push("Mahesh",8)
p2.push("Jay",4)
print("No of elements are = ",p2.size())

while not p2.is_empty():
    print(p2.pop())

print(p2.is_empty())

        
        
