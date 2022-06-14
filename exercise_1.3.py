def sum_of_max_squ(a, b, c):
    if a >= b >= c or  b >= a >= c:
        return add(squ(a), squ(b))

    elif a >= c >= b or c >= a >= b:
        return add(squ(a), squ(c))

    elif c >= b >= a or b >= c >= b:
        return add(squ(b), squ(c))

def add(a, b):
    return a + b

def  squ(a):
    return a**2