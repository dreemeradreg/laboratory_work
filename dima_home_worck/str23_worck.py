
def int_to_roman(n):

    if not 0 < n < 4000:
        print("нельзя указать меньше 1 и больше 3999") 

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = int(n / ints[i])
        result += nums[i] * count
        n -= ints[i] * count
    print(result)


n = int(input("введи натуральное число:"))
int_to_roman(n)
