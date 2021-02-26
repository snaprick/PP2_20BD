n = int(input())
s = str(input())
for i in s:
    c = ord(i)+n
    if c > 90:
        c=c%90+64
    #print(c,end = " ")
    print(chr(c), end='')