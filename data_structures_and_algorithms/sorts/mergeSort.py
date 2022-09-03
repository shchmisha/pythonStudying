# merge sort is a divide and conquer alogorithm
# Divide the input array in two halves and we keep halving recursively until they
# become too small and cannot be broken down further
# mergehalves by sorting them

def merge(list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0]*n1
    R = [0]*n2

    for i in range(0, n1):
        L[i] = list[l+i]

    for j in range(0, n2):
        L[j] = list[m+1+j]

    i = 0
    j = 0
    k = l
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j+=1
        k+=1
    while i<n1:
        list[k] = L[i]
        i += 1
        k+=1
    while j<n2:
        list[k] = R[j]
        j+=1
        k+=1

def merge_sort(list, l, r):
    if l<r:
        m = (l+(r-1))//2
        merge_sort(list, l, m)
        merge_sort(list, m+1, r)
        merge(list, l, m, r)
    return list


def mergeSort(arr):
    if len(arr)>1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i = 0
        j = 0
        k = 0
        while i<len(leftArr) and j<len(rightArr):
            if leftArr[i]<rightArr[j]:
                arr[k]=leftArr[i]
                i+=1
            else:
                arr[k]=rightArr[j]
                j+=1
            k+=1

        while i<len(leftArr):
            arr[k]=leftArr[i]
            i+=1
            k+=1

        while j<len(rightArr):
            arr[k]=rightArr[j]
            j+=1
            k+=1


list = [2,6,3,5,4,7,9,1]
mergeSort(list)
print(list)