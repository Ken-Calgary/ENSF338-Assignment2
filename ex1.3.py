prev_result = {}

def func(n):
    if n == 0 or n == 1:
        return n
    
    if n not in prev_result:
        prev_result[n] = func(n - 1) + func(n -2)
    
    return prev_result[n]
