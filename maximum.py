def max(data):
    _max = data[0]
    i = 1
    while i < len(data):
        if data[i] > _max:
            _max = data[i]
        i += 1
    return _max