import math

def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False

	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False

	return True

def is_hyper_prime(n):
	while n > 0:
		if not is_prime(n):
			return False
		n = n // 10
	return True


i = int(input("введите натуральное число: "))
if is_hyper_prime(i) == True:
	print("число "+str(i)+" гиперпростое")
else:
	print("число "+str(i)+" не гиперпростое")

