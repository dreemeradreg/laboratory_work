
def function(a,b):
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a

	nod = a + b
	return nod


a,b = map(int, input("введите 2 числа:  ").split())

print(a,", ", b," = ",function(a,b))