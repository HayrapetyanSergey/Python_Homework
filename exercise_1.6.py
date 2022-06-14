def sum(a , b):
    sum = 0

    if a < b:
        while a != b - 1:
            sum += a + 1
            a = a + 1
    
    elif b < a:
        while b != a-1:
            sum += b+1
            b = b + 1
    
    else:
        return "hasn't number"
      
    return sum