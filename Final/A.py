n,m = map(int,input().split())
a = list()
def check(m):
    while m % 3 == 0:
        m //= 3
    if m == 1:
        return True
    else:
        return False
for i in range(n,m+1):
    if check(i) and len(str(i))== 4:
        a.append(i)
print(*a[::-1])