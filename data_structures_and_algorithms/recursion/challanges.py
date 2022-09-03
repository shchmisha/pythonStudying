# POWER SOLUTION
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
# FACTORIAL SOLUTION
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
# PRODUCT OF ARRAY SOLUTION
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
# RECURSIVE RANGE SOLUTION
def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)
# FIBONACCI SOLUTION
def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)

# REVERSE SOLUTION
def reverse(strng):
    if len(strng) <= 1:
      return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
# IS PALINDROME SOLUTION
def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])
# SOME RECURSIVE SOLUTION
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True
 
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
# FLATTEN SOLUTION
def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr

# CAPITALIZE FIRST SOLUTION
def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:]) 
# NESTED EVEN SUM SOLUTION
def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum
# CAPITALIZE WORDS SOLUTION
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])
# STRINGIFY NUMBERS SOLUTION
def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj
# COLLECT STRINGS SOLUTION
def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr
