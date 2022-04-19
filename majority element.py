
def func(arr):
    b=dict()
    l=len(arr)/2
    for i in arr:
        if i not in b.keys():
            b[i]=1
        else:
       
             b[i]=b[i]+1
        
    for i in b:
        if b[i]>l:
            return i 

    return -1


v=func([2,2,1,1,1,2,2])
print(v)


