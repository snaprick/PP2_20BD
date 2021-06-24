n,m = map(int,input().split())
mx = -1
mi = 0
for i in range(n):
    sum = 0
    a = list(map(int,input().split()))
    for j in a:
        sum+=j
    if sum > mx:
        mx = sum
        mi = i
print(mi+1)