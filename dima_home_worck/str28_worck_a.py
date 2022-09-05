

def function(a,b,c):
	Natural_numbers = [a,b,c]
	Natural_numbers.sort()
	return Natural_numbers

a,b,c =  map(int, input("введите 3 числа: ").split())
print(function(a,b,c))
