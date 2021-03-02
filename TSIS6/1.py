def mx(a,b,c):
    if a>=b:
        if c>=a:
            return c
        else:
            return a
    else:
        if c >=b:
            return c
        else:
            return b
a,b,c = map(int,input().split())
print(mx(a,b,c))