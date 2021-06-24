def check(m):
    while m % 2 == 0:
        m //= 2
    if m == 1:
        return True
    else:
        return False
a = list(map(int,input().split()))
s = list()
for i in a:
    if check(i):
        s.append(i)
print(*sorted(set(s)))