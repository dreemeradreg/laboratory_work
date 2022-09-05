

a = int(input("введи от чего:"))
b = int(input("введи до чего:"))

j = 0
for x in range(a,b+1):
	
	for i in range(2, x):
		if x % i == 0:
			j = j + 1

	if j == 0:
		print(x)
	else:
		j = 0
