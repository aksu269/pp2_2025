def func(n):
    num = 0
    while num <= n:
        if num % 3 == 0 or num % 4 == 0:
            yield num
        num += 1
nums = func(54)
for x in nums:
    print(x)