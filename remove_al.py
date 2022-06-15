from os import remove

def _remove_all(data, value):
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(data[i])
        i += 1
