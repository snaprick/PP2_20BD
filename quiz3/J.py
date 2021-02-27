n = int(input())
a = list(map(int,input().split()))
if n==1:
    print("Clean:1\nDirty:0")
else:
    print("Clean:0\nDirty:{}".format(n))