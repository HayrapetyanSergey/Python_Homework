def join(data, sep):
    new_str = ''
    for i in data:
        new_str += i + sep
    return new_str

print(join(['Hello','!'],'word'))
