sm = 0
nl = 1
n = 1
while n < 4000000:
    x = n
    n = n + nl
    nl = x
    if n%2 == 0: sm += n
print(sm)
