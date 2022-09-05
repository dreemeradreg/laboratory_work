#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random

def worck_1():

	l = list()
	list_rand = list()
	list_rand_new = list()
	b = 0
	for x in range(5):
		rand_int = random.randint(-10, 10)
		list_rand.append(rand_int)
		b += rand_int


	print("*"*30+"\n**********1 задание***********n"+"*"*30)
	print("список с рандомными числами:  ",list_rand)
	print("средне арефметическое списка: ",b/5)	
	print("реверс списка:                ",list_rand[::-1])

	for x in list_rand:
		if x >= 0:
			list_rand_new.append(-x)

	"""
	тож самое но в виде генератора
	[l.append(-x) for x in list_rand if x >=0]
	print(l)
	"""
	print("новый список из отрицательных без прошлых отрицательных ",list_rand_new)		
	print("*"*30)

def worck_2():
	print("*"*30+"\n**********2 задание***********\n"+"*"*30)

	list_rand = list()
	list_rand_new = list()
	
	l = []
	l_n = []
	n_list = []


	[list_rand.append(random.randint(-10, 50)) for x in range(10)]
	[list_rand_new.append(random.randint(-10, 50)) for x in range(10)]

	# print("2 списка не отсортированных")
	# print(list_rand)
	# print(list_rand_new)
	print("2 отсортированных списка")
	l = sorted(list_rand)
	l_n = sorted(list_rand_new)
	print("1 список ",l)
	print("2 список ",l_n)

	n_list = l_n
	[n_list.append(x) for x in l]
	
	print("\nне отсортированный: ",n_list)

	for i in range(19):
		for j in range(19-i):
			if n_list[j] > n_list[j+1]:
				n_list[j], n_list[j+1] = n_list[j+1], n_list[j]

	print("\nот сартированный: ",n_list,"\n")

def worck_3():
	print("*"*30+"\n**********3 задание***********\n"+"*"*30)

	coordinates = [[1,1],[3,2],[6,7]]
	i = 0
	j = 1
	len_list = []
	while i < len(coordinates):
		if (i == 2):
			j = 0
		a = ((coordinates[i][0] - coordinates[j][0]) ** 2
		+ (coordinates[i][1] - coordinates[j][1]) ** 2) ** (1 / 2)
		len_list.append(a)
		j += 1
		i += 1

	print("длинны сторон ",len_list)

	pirimitr = len_list[0] + len_list[1] + len_list[2]
	print("периметр треугольника",pirimitr)

	len_list.append(pirimitr)
	p = len_list[3] / 2

	herons_Formula = ((p * (p - len_list[0]) * (p - len_list[1]) * (p - len_list[2])) ** (1 / 2))

	print("прощадь по герону ",herons_Formula)

def main():
	worck_1()
	print()
	worck_2()
	print()
	worck_3()

if __name__ == '__main__':
	main()
