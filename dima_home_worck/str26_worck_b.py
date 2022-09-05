
def function(n):
	ot = 0
	for x in str(n):
		ot = ot+int(x)
	return ot

n = int(input("введите натуральное число: "))
print("сумма цифр числа ",n,"равна ", function(n))

