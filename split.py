def split(source, sep, count):
    str1 = ''
    lst = []
    new_count = 0
    for i in range(len(source)):
        str1 += source[i]
        if source[i] == sep and new_count < count:
            str1 = str1.replace(sep, '')
            lst.append(str1)
            str1 = ''
            new_count += 1
    lst.append(str1)        
    return lst  
  
print(split('Picsart Academy', 'c', 3))    