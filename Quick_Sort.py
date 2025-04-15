"""Quick Sort"""
def Quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot=data_list[0]
        lesser=[x for x in data_list[1:] if x<=pivot]
        greater=[x for x in data_list[1:] if x>pivot]
        return Quick_sort(lesser)+[pivot]+Quick_sort(greater)
    
l=[53,11,72,68,41,25,18,37,44,80]
l=Quick_sort(l)
print(l)