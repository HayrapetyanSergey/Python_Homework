def replace(source, old, new):
    res = ''
    lst = source.split(' ')
    for i in lst:
        if i == old:
            res += new + ' '
        else:
            res += i + ' '
    return res.strip()

print(replace('Kapan is the capital of Armenia ', "Kapan", "Yerevan"))