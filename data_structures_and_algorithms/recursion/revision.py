def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power*2

# recursion forms a pyramid of function calls and then return statements

# think of it as the factorial function
# factorial(5) = 5 * factorial(4)
# that means the
def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)

def sumOfDigs(n):
    #  f(n) = n%10 + f(n/10)
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigs(n/10)