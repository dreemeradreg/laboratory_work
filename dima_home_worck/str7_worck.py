
a = int(input("Введи возраст Антона: "))
b = int(input("Введи возраст Бориса: "))
c = int(input("Введи возраст Виктора: "))

if a >= b and a >= c:
	if b == a and b > c:
		print("Ответ: Антон и Борис старше Виктора")
	elif c == a and c > b:
		print("Ответ: Антон и Виктор старше Бориса")
	elif a == c and a == b:
		print("Ответ: у всех одинаковый возраст")
	else:
		print("Ответ: Антон старше всех")

elif b >= a and b >= c:
	if b == c and b > a:
		print("Ответ: Борис и Виктор старше Антона")
	else:
		print("Ответ: борис старше всех")

else:
	if a == c and c > b:
		print("Ответ: Антон и Виктор старше Бориса")
	else:
		print("Ответ: Виктор старше всех")
