
a = int(input("Введи 1 число: "))
b = int(input("Введи 2 число: "))
c = int(input("Введи 3 число: "))
d = int(input("Введи 4 число: "))
e = int(input("Введи 5 число: "))

if a > b and a > c and a > d and a > e:
	print("Mаксимальное число: ",a)
elif b > a and b > c and b > d and b > e:
	print("Mаксимальное число: ",b)
elif c > a and c > d and c > b and c > e:
	print("Mаксимальное число: ",c)
elif d > a and d > b and d > c and d > e:
	print("Mаксимальное число: ",d)
else:
	print("Mаксимальное число: ",e)
