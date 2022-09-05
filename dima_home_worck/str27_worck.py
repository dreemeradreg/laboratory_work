

def function(n):
	i=len(str(n))
	n = str(n)
	ot = ''
	while i > 0:
		ot = ot + str(n[i-1])
		i -= 1
		
	return ot

n = int(input("введите нартулаьное число:"))
print("после переворота: ", function(n))

