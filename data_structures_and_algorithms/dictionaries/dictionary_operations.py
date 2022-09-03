myDict = {'name': 'Misha', 'age': 19, 'address': 'London', 'profession': 'developer'}


# in
# checks whether a key is present in a dictionary
print('name' in myDict)
print('Misha' in myDict.values())

# all
# checks whether all given elements of an iterable are true

# sorted
print(sorted(myDict, key = len))
