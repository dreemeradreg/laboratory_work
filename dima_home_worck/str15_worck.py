
n = int(input("Введи N:"))
c = 1
p = 1
s = 0
while c < n:
	s += c
	c, p = c + p, c

print("Ответ:",s)

