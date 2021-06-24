def isprime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
a = list()
n, m = map(int,input().split())
for i in range(n,m+1):
    if isprime(i):
        a.append(i)
print(*a[::-1])