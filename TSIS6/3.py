def f(a):
    prod=1
    for i in a:
        prod*=i
    return prod
n = list(map(int,input().split()))
print(f(n))