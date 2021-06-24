def check(m):
    while m % 2 == 0:
        m //= 2
    if m == 1:
        return True
    else:
        return False
a = list(map(int,input().split()))
s = set()
for i in a:
    if not check(i):
        s.add(i)
print(*s)