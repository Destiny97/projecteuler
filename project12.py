def triangle(i):
    num = 0
    for i in range(1, i+1, 1):
        num += i
    return num

def dividers(num):
    n = 0
    for i in range(1, num+1, 1):
        if num % i == 0: n += 1
    return n

div = 0
i = 1
maxx = 0
while div <= 500:
    num = triangle(i)
    div = dividers(num)
    if div > maxx:
        print("{0}. {1}: {2}".format(i, num, div))
        maxx = div
    i += 1

print(div)
