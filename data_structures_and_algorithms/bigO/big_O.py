# Big O is the language and metric we use to describe the efficiency of algorithms

def average(arr):
    sumofnum = 0
    for item in arr:
        sumofnum += item
    return  sumofnum/len(arr)

print(average([1, 2, 3]))
    