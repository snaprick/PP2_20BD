x0,y0=0,0
ok = False
s = input()
x,y = map(int,input().split())
if x0 == x and y0 == y:
        ok = True
for i in s:
    if i == "R":
        x0+=1
    if i == "L":
        x0-=1
    if i == "U":
        y0+=1
    if i == "D":
        y0-=1
    if x0 == x and y0 == y:
        ok = True
if ok:
    print("Passed")
else:
    print("Missed")