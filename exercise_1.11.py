def function(n):
    if n == 0 or n == 1 or n == 2:
        return n
    return function(n - 1) + function(n - 2) + function(n - 3)
    

def function_iter(n):
    a, b, c = 0, 1, 2
    if n < 3:
        return n
    elif n >= 3:
        while n >= 3:
            a, b, c = b, c, a+b+c
            n -= 1
    return c
