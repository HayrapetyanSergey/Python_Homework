def pop(data, index):
    
    if index == None:
        tmp = data [len(data)-1]
        del data[len(data)-1]
        return tmp

    elif 0 <= index < len(data):
        tmp = data[index]
        del data[index]
        return tmp
    
    else: 
        return "There isn't element with that index"

lst = [0,1,2,3,4,5,25]
print (pop(lst,None))
