n = int(input())
i = 2
ok = True
while i*i <= n:
	if n % i == 0:
		print(i)
		ok = False
		exit()
	i += 1
print(n)