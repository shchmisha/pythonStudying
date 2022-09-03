
# Bottom up approach:

def NumberFactor(N, dp):
    if N in (0,1,2): return 1
    if N == 3: return 2
    elif N in dp:
        return dp[N]
    else: 
        dp[N] = NumberFactor(N-1) + NumberFactor(N-2) + NumberFactor(N-4)
        return dp[N]

def numberFactor(n):
    tb = [1,1,1,2]
    for i in range(4, n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4])
    return tb[n]