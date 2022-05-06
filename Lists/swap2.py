arr=[1,2,3,4,5]
print(arr)
def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

pos1=2
pos2=5
swap(arr,pos1-1,pos2-1)
print(arr)