"""Insertion Sort"""
def Insertion_sort(data_list):
    for i in range(1,len(data_list)):
        temp=data_list[i]
    
        j=i-1
        while j>=0 and temp<data_list[j]:
            data_list[j+1]=data_list[j]
            j-=1
        data_list[j+1]=temp

l=[34,32,76,45,48,54,98,44]
Insertion_sort(l)
print(l)