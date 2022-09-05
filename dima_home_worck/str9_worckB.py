
a = int(input("Введи номер месяца: "))

if a == 1 or a == 2 or a == 12:
	print("Зима!")
elif a >= 3 and a <= 5:
	print("Весна.")
elif a >= 6 and a <= 8:
	print("Лето.")
elif a >= 9 and a <= 11:
	print("Осень")
else:
	print("Неверный номер месяца.")