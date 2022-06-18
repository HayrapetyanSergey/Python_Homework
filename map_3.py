def map3(sum, data1, data2, data3):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = sum(data1[i], data2[i], data3[i])
    return res

def sum(a,b,c):
    return a + b + c