def fast_mul(a, b):
    if b == 0:
        return 0
    if is_even(b):
        return double(a) + (fast_mul(a,b-2))
    else:
        return a + fast_mul(a, b-1)
        
def double(a):
    return 2*a

def is_even(n):
    return n % 2 == 0

print (fast_mul(5,4))