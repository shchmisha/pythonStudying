"""
Top Down With Memoisation

Solve the bigger problem by recursively finding the solution to smaller subproblems
Whenever we solve a problem, we cache it's result so that we dont end up solvinig it
repeatedly if it's called multiple times. This technique of storing the results of 
already solved problems is called Memoization
"""

def fibMemo(n, memo):
    if n==1:
        return 0
    if n==2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

myDict = {}
print(fibMemo(34, myDict), myDict)