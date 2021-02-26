n = int(input())
s = list(set())
for i in range(n):
    a = input()
    for j in a:
        s[i].add(j)
for i in s:
    print(i)
