import math	

def function(a,b):
	k = math.gcd(a,b)
	ot = a//k,b//k
	return ot

a,b =  map(int, input("введите 2 числа: ").split())
print("После сокращения ",function(a,b))
