def printeven(f):
    for i in f:
        if i%2==0:
            print(i,end=' ')
a = list(map(int,input().split()))
printeven(a)