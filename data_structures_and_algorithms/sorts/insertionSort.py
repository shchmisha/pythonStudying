def insertionSort(list):
    for i in range(1, len(list)):
        cur = list[i]
        j = i-1
        while j>=0 and cur < list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = cur
    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        while list[i] < list[i-1] and i>0:
            list[i], list[i-1] = list[i-1], list[i]
            i-=1
    print(list)

# insertion_sort([1,4,6,7,4,2,3,7,8])
# insertionSort([1,4,6,7,2,3,8])





def insert_sort(list):
    for i in range(1, len(list)):
        cur = list[i]
        j =  i - 1
        while j>=0 and cur < list[j]:
            list[j], list[j+1] = list[j+1], list[j]
            j-=1
    return list

# insertion sort:

# loops through all values
# while the current item is less than the previous, swaps them around

# 1) loop from second to last items in list
# 2) while index is greater than one and previous item is greater than current
#    swap their values
#    decrement i



def insertSort(arr):
    for i in range(1, len(arr)):
        while i>0 and arr[i-1]>arr[i]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
    return list








def isort(arr):
    for i in range(1, len(arr)):
        while i>0 and arr[i-1]>arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i-=1
    return arr

print(isort([1,4,6,7,4,2,3,7,8]))