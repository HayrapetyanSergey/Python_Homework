def pow(base, exp):

    if exp == 0:
        return 1
        
    elif base == 0 and exp < 0:
        return "Empty"

    res = 1
    count = 0
    while count < abs(exp):

        if  exp > 0:
            res = res * base
            count += 1
    
        elif exp < 0:
            res = res * (1/base)
            count += 1
    return res