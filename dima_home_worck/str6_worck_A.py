
a = int(input("Введи 1 число: "))
b = int(input("Введи 2 число: "))
c = int(input("Введи 3 число: "))

if a > b and a > c:
	print("Mаксимальное число: ",a)
elif b > a and b > c:
	print("Mаксимальное число: ",b)
else:
	print("Mаксимальное число: ",c)
