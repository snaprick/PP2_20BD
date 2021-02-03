a = str(input())
ans=""
ans+=a[(len(a)+1)//2:]
ans+=a[:(len(a)+1)//2]
print(ans)