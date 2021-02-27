n,m = map(int,input().split())
ok = False
for i in range(n):
    a,b,c = map(int,input().split())
    if (a+b+c)/3>=m:
        ok= True
if ok:
    print("YES")
else:
    print("NO")