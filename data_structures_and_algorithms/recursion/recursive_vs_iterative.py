# recursive

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

# print(powerOfTwoIt(5))
# print(powerOfTwo(5))


# n! = n * (n-1)!
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number has to be a  string and  cannot be less than one'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))