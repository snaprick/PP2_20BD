def f(a):
    sum=0
    for i in a:
        sum+=i
    return sum
n = list(map(int,input().split()))
print(f(n))