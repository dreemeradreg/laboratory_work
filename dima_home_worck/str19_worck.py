
N = int(input("Введи N: "))

mod = 10
for i in range(1, N + 1):
    if i == mod:
        mod *= 10
    if (i * i) % mod == i:
        print(i,"*",i,"=",i*i)
        