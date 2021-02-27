s = list(map(str,input().split()))
mx=-1
ms=""
for i in s:
    if len(i)>mx:
        mx = len(i)
        ms=i
print(ms,mx,sep="\n")