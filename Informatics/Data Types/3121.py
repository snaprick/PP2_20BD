s = str(input())
if s.find("f") == -1:
    print(-2)
    exit()
c = s.replace("f","",1)
if c.find("f") == -1:
    print(-1)
    exit()
else:
    print(c.find("f")+1)