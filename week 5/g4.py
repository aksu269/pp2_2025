def squares(a, b):
    while a <= b:
        yield a**2
        a += 1
nums = squares(1, 9)
for x in nums:
    print(x)