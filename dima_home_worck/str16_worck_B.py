
a = int(input("Введи натуральное целое число: "))
o = 0
j = 0
for x in str(a):
	if o == int(x):
		j += 1
	o = int(x)

if j > 0:
	print("ДА")
else:
	print("Нет.")
