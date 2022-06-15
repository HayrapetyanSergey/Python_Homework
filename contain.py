def is_contain(data, value):
    i = 0
    while i < len(data):
        if data[i] == value:
            return True
        i += 1
        return False