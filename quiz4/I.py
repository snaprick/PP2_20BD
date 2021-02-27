n = int(input())
a = list(map(str,input().split()))
k = int(input())
ans=""
ans1=""
if k == 0:
    print(0)
    exit()
for i in a[0:k]:
    ans+=i
for i in a[k:]:
    ans1+=i
print(int(ans)*int(ans1))