import math
def IsPointInCircle(x, y, x1, y1, r):
    return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)<=r
a = float(input())
b = float(input())
x = float(input())
y = float(input())
r = float(input())
if IsPointInCircle(a, b, x, y, r):
    print("YES")
else:
    print("NO")