n = int(input())
a = list(map(str,input().split()))
st = dict()
m = int(input())
a1 = list(map(str,input().split()))
st1 = dict()
ans,ans1 = list(),list()
for i in a:
    if i not in a1:
        ans.append(i)
for i in a1:
    if i not in a:
        ans1.append(i)
print("Missed students:")
for i in ans:
    print("-",i)
print("Not in the group:")
for i in ans1:
    print("-",i)

