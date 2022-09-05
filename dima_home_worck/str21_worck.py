
x = int(input("введи N: "))

for x in range(1,x+1):
	if str(0) not in str(x):
		if len(str(x)) < 2: 
			if x % x == 0:
				print(x) 
		elif len(str(x))>1:
			f = str(x) 
			if x % int(f[1]) == 0:
				print(x)

