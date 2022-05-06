arr=[12,35,9,56,24]
def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    
swap(arr,0,len(arr)-1)
print(arr)