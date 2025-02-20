def squares(n):
    temp = 1
    while temp**2 <= n:
        yield temp ** 2
        temp += 1
n = squares(25)
for x in n:
    print(x)
