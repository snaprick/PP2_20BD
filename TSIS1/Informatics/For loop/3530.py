n = int(input())
a = 10 ** (n - 1)
b = 10 ** n - 1
for i in range(b, a - 1, -2):
	print(i, end = " ")