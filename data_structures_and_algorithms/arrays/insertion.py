from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.1,1.2,1.3])

# insert attheend
arr1.insert(6,7)
# insert in the begginning
arr1.insert(0,0)
# insert a t an index
arr1.insert(2,4)
# insertion at an index moves the other one space to the right and inserts the value  at the specified index

arr1.remove(3)


print(arr1)