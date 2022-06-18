def map(pow, data1, data2):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = pow(data1[i], data2[i])
    return res

def pow(base, exp):
    res = 1
    count = 0
    while count < exp:
        res *= base
        count += 1 
    return res

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (map(pow, list1, list2))