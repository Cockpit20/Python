def cyclicSort(arr):
    i=0
    while i<len(arr):
        if arr[i]!=i+1:
            swap(arr,i,arr[i]-1)
        else:
            i+=1

def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

arr=[6,2,5,3,1,4]
cyclicSort(arr)
print(arr)