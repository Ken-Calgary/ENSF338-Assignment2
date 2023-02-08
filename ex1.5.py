# Time the original code and your improved version, for all integers between 0 and 35,
# and plot the results.

prev_result = {}

def improved_func(n):
    if n == 0 or n == 1:
        return n
    
    if n not in prev_result:
        prev_result[n] = improved_func(n - 1) + improved_func(n -2)
    
    return prev_result[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else: 
        return func(n - 1) + func (n -2)