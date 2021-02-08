n = int(input())
dx,dy = 1,0           
x,y = 0,0              
a = [[0]* n for j in range(n)]
for i in range(1,n**2+1):
    a[x][y] = i
    nx,ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n and a[nx][ny] == 0:
        x,y = nx,ny
    else:
        dx,dy = -dy,dx
        x,y = x+dx, y+dy
n = range(len(a))
for y in n:
    for x in n:
        print (a[x][y],end=' ')
    print()