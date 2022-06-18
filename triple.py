def triple(data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = data[i] * 3
    return res