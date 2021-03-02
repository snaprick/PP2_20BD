def check(s):
    st = list()
    for i in s:
        if i.lower() not in st and i.isalpha():
            st.append(i.lower())
    #print(st)
    return len(st)==26
n = input()
if check(n):
    print("YES")
else:
    print("NO")