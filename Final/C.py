n = list(map(int,input().split()))
a = list()
cnt = 0
for i in n:
    if i == 0:
        cnt+=1
    else:
        a.append(i)
print(*a,end = " ")
print("0 "*cnt)