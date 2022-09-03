"""
Bottom Up with Tabulation

Tabulation is the opposite of the top down approach and avoids recursion. In this approach,
we solve the problem 'bottom up' (by solving subproblems first). This is done by filling up a table.
Based on the results in the table, the solution to the top/original problem is computed
"""

def fibonacciTab(n):
    tb = [0,1]
    for i in range(2, n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]