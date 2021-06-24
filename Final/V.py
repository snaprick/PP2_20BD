a,b,k = map(int,input().split())
n = list()
for i in range(1,max(a,b)+1):
    if a%i == 0 and b%i == 0:
        n.append(i)
print(n[len(n)-k])