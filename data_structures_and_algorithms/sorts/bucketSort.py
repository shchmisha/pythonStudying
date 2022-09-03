

import math
from insertionSort import insertionSort

def bucketSort(list):
    buckets = round(math.sqrt(len(list)))
    max_value = max(list)
    arr = []

    for i in range(buckets):
        arr.append([])

    for j in list:
        index_b = math.ceil(j*buckets/max_value)
        arr[index_b-1].append(j)
    
    for i in range(buckets):
        arr[i] = insertionSort(arr[i])

    counter = 0
    for i in range(buckets):
        for j in range(len(arr[i])):
            list[counter] = arr[i][j]
            counter+=1

    return list

print(bucketSort([1,4,6,7,4,2,3,7,8]))