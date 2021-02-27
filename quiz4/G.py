import re
txt = input()
t = input()
s = input()
f = input()
txt = re.sub(t,s,txt)
ans = re.findall(f,txt)
print(len(ans))