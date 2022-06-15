def reverse(data):
    i = 0
    while i < len(data) // 2:
        data[i], data[-1-i] = data[-1-i], data[i]
        i += 1