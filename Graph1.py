"""Adjacency Matrix Graph"""
class Graph:
    def __init__(self,vno): # vno=total number of vertex
        self.vertex_count=vno
        self.adj_matrix=[ [0]*vno for e in range(vno) ] #vno*vno matrix
    def add_edge(self,u,v,weight=1): # u=starting vertex,v=ending vertex
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid vertex")
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid vertex")
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid vertex")
    def print(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))            
#Driver code
g1=Graph(5)
g1.add_edge(0,1)
g1.add_edge(1,2,"M")
g1.add_edge(1,3)
g1.add_edge(2,3)
g1.add_edge(3,4)
g1.print()
print()
g1.remove_edge(3,1)
g1.print()
print(g1.has_edge(0,1))
        