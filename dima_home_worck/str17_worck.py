

a = int(input("Введи натуральное целое число: "))
i = 0
str_mass = str(a)

for x in str(a):
	str_mass = str_mass[1:]
	
	if x in str_mass:
		i += 1

if i > 0:
	print("ДА")
else:
	print("Нет.")



