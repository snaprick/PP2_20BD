n = int(input())
h = n//3600%24
m = (n%3600)//60%60
s = n%60
if m < 10:
    m = '0'+str(m)
if s < 10:
    s = '0'+str(s)
print(str(h)+':'+str(m)+':'+str(s))