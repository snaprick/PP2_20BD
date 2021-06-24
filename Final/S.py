n = int(input())
a = list(map(int,input().split()))
mx = max(a)
for i in a:
    if i == mx:
        print(1,end=" ")
    else:
        print(0,end=" ")