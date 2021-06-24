import math
h,a,b = map(int,input().split())
ans = 0
cnt = 0
while True:
    cnt+=1
    ans+=a
    if ans>=h:
        break
    ans-=b
print(cnt)