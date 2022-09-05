
print("Введите 2 целых числа при условии, что 0 > 1 числа > 2 числа ")
a = int(input("Введи 1 число: "))
b = int(input("Введи 2 число: "))

while a <= b:
	c = a*b
	print(str(a)+"*"+str(b)+"="+str(c))
	a +=1
