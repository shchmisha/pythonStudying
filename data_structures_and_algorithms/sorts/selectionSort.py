def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range (i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j 
        list[i], list[min_index] = list[min_index], list[i]
    print(list)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr