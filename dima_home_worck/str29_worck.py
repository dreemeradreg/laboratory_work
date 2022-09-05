import math


def function(a,b):
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a

	nod = a + b
	return nod

def lcm(a, b):
  	m = a * b
  	nok = m / function(a,b)
  	return int(nok)


a,b = map(int, input("введите 2 числа:  ").split())

print("НОД",a,", ", b," = ",function(a,b))
print("НОк",a,", ", b," = ",lcm(a,b))
