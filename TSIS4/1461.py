b = list(map(int, input().split()))
b+=[-2]
del b[0]
cnt = 1
for i in range(len(b) - 1):
    if b[i] == b[i + 1]:
        cnt+=1
    else:
        if cnt>=3:
            b[i+1-cnt:i+1]=[-1]*cnt
        cnt = 1
#print(*b)
print(len([i for i in b if i == -1]))
#0 1 2 3 4 5
#1 1 1 4 5 6