"""Merge Sort"""
def Merge_Sort(data_list):
    if len(data_list)>1:
        mid=len(data_list)//2
        leftlist=data_list[:mid]
        rightlist=data_list[mid:]
    
        Merge_Sort(leftlist)
        Merge_Sort(rightlist)
        
        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                data_list[k]=leftlist[i]
                i+=1
            else:
                data_list[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            data_list[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            data_list[k]=rightlist[j]
            j+=1
            k+=1

l=[75,29,83,42,16,90,56,34,20,71,88,92,7]
Merge_Sort(l)
print(l)
            
            