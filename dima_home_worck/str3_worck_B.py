import math

a1 = float(input("В веди 1 координату А: "))
a2 = float(input("В веди 2 координату А: "))

b1 = float(input("В веди 1 координату B: "))
b2 = float(input("В веди 2 координату B: "))

d=math.sqrt((b2-a2)*(b2-a2)+(b1-a1)*(b1-a1))
# d=math.sqrt((b2-a2)**2+(b1-a1)**2) #аналогично выше написанному
print("Ответ задачи: ", d)

