entry = list()

def ing_inp():
    while 1:
        x = inp('Enter an ingredient or enter done to continue\n')
        if (x=='done'):
            break
        entry.append(x)
        
    return entry
        