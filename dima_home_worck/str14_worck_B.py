
print("Введите 2 целых числа")
a = int(input("Введи 1 число: "))
b = int(input("Введи 2 число: "))

c = 0
if a > 0 and b < 0:
	f = b 
	while b < 0:
		c=c+a
		b += 1
	print(a,"*(",f,")=",-c)
elif b > 0 and a < 0:
	f = a
	while a < 0:
		c=c+b
		a += 1
	print("(",f,")*",b,"=",-c)
elif a > 0 and b > 0:
	f = a
	while a > 0:
		c=c+b
		a -= 1
	print(f,"*",b,"=",c)
else:
	f= a
	while a < 0:
		c=c+b
		a += 1
	print("(",f,")*(",b,")=",-c)
