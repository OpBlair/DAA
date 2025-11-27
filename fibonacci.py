#Top down implementation of fibonacci
def fib(n, memo=None):
    #base case
    if n <= 1:
        return n
    if memo is None:
        memo = {}
        
    #check for n in memoization table
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))
