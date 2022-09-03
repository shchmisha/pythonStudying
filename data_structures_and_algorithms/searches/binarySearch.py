# binary search divides list into two halves, and checks in which half is the value
# continues to half the array until the middle value i sthe value being searched for
import math

def binSearch(arr, val):
    start = 0
    end = len(arr)-1
    mid = math.floor((start+end)//2)   

    while val != arr[mid]:
        if val > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = math.floor((start+end)//2)
    if arr[mid] == val:
        print(mid) 
    else:
        print(-1)
            
def binarySearch(arr, val):
    # print(arr)
    start = 0
    end = len(arr)-1
    mid = math.floor((start+end)//2)

    while not(arr[mid] == val):
        if val<arr[mid]:
            end = mid -1
        else:
            start = mid+1
        mid = math.floor((start+end)//2)
    if arr[mid] == val:
        return mid
    else:
        return -1

binarySearch([1,2,3,4,5,5,5,6,7,8,9], 6)