
a = str(input("Введи 3 числa через пробел: "))

print(a)

b = 0
for x in a:
	if x == a[0]:
		b +=1


if b == 1:
	b = 0
	for x in a:
		if x == a[2]:
			b+=1
	if b == 1:
		print("все числа разные")
	elif b ==2:
		print("2 числа одинаковы")

elif b == 2:
	print("два числа одинаковы")
else:
	print("все числа одинаковые")