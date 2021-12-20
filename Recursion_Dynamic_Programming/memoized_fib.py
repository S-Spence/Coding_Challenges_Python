

memo = {}
def fibonacci(n):
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        f = 1
    else:
        f = fibonacci(n-1) + fibonacci(n-2)
    memo[n] = f
    return f

print(fibonacci(7))
print(memo)

# this gets to linear time. The best algotim uses log(n) for computing fib
# My book does not even cover this. MIT 603 does he says in the lecture





