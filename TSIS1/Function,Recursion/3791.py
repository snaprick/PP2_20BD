import math
def f(x,y,x1,y1):
    return math.sqrt((x-x1)**2+(y-y1)**2)
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(f(a,b,c,d))