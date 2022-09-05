
for i in range(10000,100000):
	a = i%133
	b = i%124
	if a == 125 and b == 111:
		print(i)
