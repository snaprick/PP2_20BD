import sys
s = list(map(int,(sys.stdin.read()).split()))
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
d = dict()
for i in s:
    if not isprime(i):
        d[i] = d.get(i,0)+1
for i in d.keys():
    if d[i] > 1:
        a.append(i)
print(*sorted(a))