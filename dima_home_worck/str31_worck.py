
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def function(a, b):
    return gcd(a, b) == 1



a,b = map(int, input("введите 2 числа:  ").split())

if function(a,b) == True:
	print(a,"и", b,"взаимопростые")
else:
	print(a,"и", b,"не взаимопростые")