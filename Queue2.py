"""Queue using Singly Linked List"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0 
    def is_empty(self):
        return self.front==None 
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the Queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the Queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
            
        
#Driver code
q2=Queue()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
q2.enqueue(40)
print("Front=",q2.get_front(),"Rear=",q2.get_rear())
q2.dequeue()
print("Front after dequeue",q2.get_front())
print(q2.size())