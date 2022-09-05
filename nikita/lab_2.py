#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random

def worck1():
	print("*"*30+"\n**********1 задание***********\n"+"*"*30)
	a = set()
	b = set()

	[a.add(random.randint(1, 20)) for x in range(10)]
	[b.add(random.randint(1, 20)) for x in range(5)]


	print(a)
	print(b)
	# print(b in a)
	print()
	for x in b:
		if x in a:
			print(x,"принадллижит множеству")
		else:
			print(x,"не принадлежит")

	print()
	print("пересечение множеств",a.intersection(b))
	print("обьединение множеств",a.union(b))
	print("разность множеств   ",a.difference(b))
	print("множество эллементов",a.symmetric_difference(b))

def worck2():
	print("*"*30+"\n**********2 задание***********\n"+"*"*30)
	a = []
	b = []
	h = []
	# print(type(a))

	[a.append(random.randint(1, 10)) for x in range(5)]
	[b.append(random.randint(1, 10)) for x in range(5)]

	print("1 список ",a)
	print("2 список ",b,"\n")
	h = list(set(a))
	print("различных чисел содержиться в списке: ",len(list(set(a)))+len(list(set(b))))
	# print(len(list(set(b))))
	n_list = a
	[n_list.append(x) for x in b]
	# print(n_list)
	print("сумарно в списках различных чисел:    ",len(list(set(n_list))))
	print("по порядку      ",list(set(n_list)))

	d = list(set(b))
	i = 0
	while len(d) > i:
		if d[i] in h:
			h.remove(d[i])
		i +=1
	print("удалив числа из 1 списка осталось :  ", h,"\n")

def worck3():







def main():
	worck1()
	print()
	worck2()
	print()
	worck3()

if __name__ == '__main__':
	main()


