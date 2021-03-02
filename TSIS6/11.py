def check(n):
    div = 0
    sum = 0
    for i in range(n,0,-1):
        if n%i==0 and i!=n:
            div+=i
        if n%i == 0:
            sum+=i
    if div==n and sum//2==n:
        return True
    else:
        return False
n = int(input())
if check(n):
    print("YES")
else:
    print("NO")