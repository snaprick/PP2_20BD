n = int(input())
cnt=0
ok=0
for i in range (0,n+1):
    for j in range (0,i):
        cnt+=1
        print(i,end=' ')
        if cnt==n:
            ok=-1
            break
    if ok == -1:
        break