def modify_list(l):
    i = len(l)-1
    while i!=-1:
        if l[i]%2:
            del l[i]
        else:
            l[i]=l[i]//2
        i -=1
    return