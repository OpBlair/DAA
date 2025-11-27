#Bottom up implementation of fibonacci
def fib(n):
    if n <= 1:
        return n
    
    #initialize the DP table
    dp = [0] * (n + 1)
    dp[1] = 1
    
    #fill table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]
    
print(fib(6))
