arr=[36,15,10,4,64,3,2]

def selectionSort(arr):
    for i in range(len(arr)):
        correctIndex=len(arr)-1-i
        maxIndex=findMax(arr,correctIndex)
        swap(arr,correctIndex,maxIndex)

def findMax(arr,lastIndex):
    max=arr[0]
    maxIndex=0
    for i in range(lastIndex+1):
        if arr[i]>max:
            max=arr[i]
            maxIndex=i
    return maxIndex

def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

selectionSort(arr)
print(arr)