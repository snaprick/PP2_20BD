import math
def IsPointInSquare(x, y):
    return abs(x)>=0 and abs(x)<=1 and abs(y)>=0 and abs(y)<=1
a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")