s = list(input().split())
a = list()
b = set()
for i in s:
    if not (i == i[::-1]):
        b.add(i)
print(*sorted(b),sep="\n")