n = int(input())
a = list(map(int,input().split()))
b = sorted(a,key=int)
ok = True
for i in range(n):
    if a[i] !=b[i]:
        ok = False
if ok: 
    print("Interesting")
else:
    print("Not interesting")