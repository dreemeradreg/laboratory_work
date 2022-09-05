

def function(i):
	s = 0
	for j in range(1,i):
		if i%j == 0:
			s += j
		if s == i:
			ot = "число "+str(i)+" совершенное"
		else:
			ot = "число "+str(i)+" не совершенное"
	return ot

i = int(input("введите натуральное число: "))
print(function(i))
