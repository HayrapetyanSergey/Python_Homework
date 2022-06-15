def min(data):
    _min = data[0]
    i = 1
    while i < len(data):
        if data[i] < _min:
            _min = data[i]
        i += 1
    return _min
