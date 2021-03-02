def f(a):
    def f1(b):
        nonlocal a
        a += 1
        return a+b**2
    return f1
a = f(4)
print(a(4))