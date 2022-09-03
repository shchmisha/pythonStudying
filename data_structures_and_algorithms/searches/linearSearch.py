
def linearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

arr = [2,3,4,5,6]
print(linearSearch(arr, 1))