arr=[36,15,10,4,64,3,2]

def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[j-1]:
                swap(arr,j,j-1)

def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

selectionSort(arr)
print(arr)
