
a15 = 15 
b17 = 17
c21 = 21
N185 = 185

count = 0
for i in range(0, int(N185/a15) + 1):
	for j in range(0, int(N185/b17) + 1):
		for n in range(0, int(N185/c21) + 1):

			if a15*i + b17*j + n*c21 == N185:

				print("по 15кг:",i,"  по 17кг:",j,"  по 21кг: ",n)
				count = count + 1

print("всего возможно способов: ",count," сумарной на 185кг")
