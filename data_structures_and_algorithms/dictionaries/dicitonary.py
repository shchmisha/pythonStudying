myDict = {'name': 'Misha', 'age': 19}

# change values of a key by overriding them
myDict['age']= 20

# add a key/value pair by using the assignment operator
myDict['address'] = 'London'


# traverse through a dictionary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])


# search through a dictionary by value
def searchDictVal(dict, val):
    for key in dict:
        if dict[key] == val:
            return  key, val

# search through a dictionary by key
def searchDictKey(dict, val):
    for key in dict:
        if key == val:
            return  key, dict[key]

# delete/remove key/value pairs from a dict by key
# print(myDict.pop('address'))
# print(myDict.popitem())
# myDict.clear()
del myDict['address']



print(myDict)
# traverseDict(myDict)
# print(searchDictVal(myDict, 20))
# print(searchDictKey(myDict, 'age'))