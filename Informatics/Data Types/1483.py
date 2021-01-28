a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))
ans = (b[0]-a[0])*3600 +(b[1]-a[1])*60+(b[2]-a[2])
print(ans)