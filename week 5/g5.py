def nums(n):
    while n >= 0:
        yield n
        n -= 1
numbers = nums(5)
for x in numbers:
    print(x)