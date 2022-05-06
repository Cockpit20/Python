arr=[36,15,10,4,64,3,2]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(1,len(arr)-i):
            if arr[j]<arr[j-1]:
                swap(arr,j,j-1)

def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

bubbleSort(arr)
print(arr)
