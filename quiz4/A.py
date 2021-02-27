a=int(input())
b=int(input())
c=int(input())
d=int(input())
ans = list()
for i in range(a,b):
    if i%d==c:
        ans.append(i)
print(*ans,sep="\n")