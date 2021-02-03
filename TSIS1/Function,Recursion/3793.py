import math
def IsPointInSquare(x, y):
    return (abs(x)+abs(y))<=1
a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")