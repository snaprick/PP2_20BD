def ispal(f):
    s = f[::-1]
    for i in range(0,len(f)):
        if s[i]!=f[i]:
            return False
    return True
n = input()
if ispal(n):
    print("YES")
else:
    print("NO")
    