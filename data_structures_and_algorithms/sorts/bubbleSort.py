




def bubble_sort(list):
    indexing_length = -1
    sorted = False

    while not sorted:
        sorted = True
        # iterate over the list until each value is lower than the next
        # subtract one from length because we do not have a next value to compare it with 
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                sorted= False
                list[i], list[i+1] = list[i+1], list[i]
    return list

def bubbleSort(list):
    for i in range(len(list)-1):
        # len(list)-i-1 because the last element after each iteration is considered sorted
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)


        
        
            