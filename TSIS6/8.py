def f(a):
    st = list()
    for i in a:
        if i not in st:
            st.append(i)
    return st
n = list(map(int,input().split()))
print(f(n))