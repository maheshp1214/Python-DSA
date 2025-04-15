"""Singly linked list"""
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next 
    
class SLL:
    def __init__(self,start=None):
        self.start = start      
    def is_empty(self):
        return self.start==None   
    def insert_at_start(self,data):
        n=Node(data,self.start) #new node
        self.start=n 
    def insert_at_last(self,data):
        n=Node(data) #new node where next is already None
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None: #first node to delete
            self.start=self.start.next #skip first element and refer 2nd node in start
    def delete_last(self):
        if self.start is None: #empty list
            pass
        elif self.start.next is None: #if only one node here to delete
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:#for more than one node
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None: #empty list
            pass
        elif self.start.next is None: # only one node in the list
            if self.start.item==data: #match data with node item
                self.start=None
        else:
            temp=self.start
            if temp.item==data: #to delete first node among all nodes
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLIterator(self.start) #this start is linked list start

class SLLIterator:
    def __init__(self,start): #this start is not linked list start
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current: #it will continue till None
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
        
                                
            

#Driver code
# mylist=SLL()
# mylist.insert_at_start(20)
# mylist.insert_at_start(10)
# mylist.insert_at_last(30)
# mylist.insert_after(mylist.search(20),25)
# mylist.print_list()
# print()
# mylist.delete_item(20)
# mylist.insert_at_last(40)
# mylist.insert_after(mylist.search(30),35)
# for x in mylist:
#     print(x,end=" ")
# print()
# print(mylist.search(55))

    

        
                
    
    
    
    