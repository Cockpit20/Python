arr=[10,20,80,30,60,50,110,100,130,170]
target=170

def binarySearch(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int(start+(end-start)/2)
        if arr[mid]==target:
            return mid
        if target>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1

print("Found at index",binarySearch(arr,target))