import numpy as np

twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# row: axis = 0, col: axis =  1
newarr_col=np.insert(twoDArray, 0, [[4,3,6,4]], axis=1)
newarr_row=np.insert(twoDArray, 0, [4,3,6], axis=0)
# print(newarr)

def getItem(array, row, col):
    print(array[row][col])

def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# getItem(newarr, 3, 2)
# traverse(twoDArray)

def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                print(i, j)

search(twoDArray, 3)