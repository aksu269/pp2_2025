def even(n):
    temp = 0
    while (temp <= n):
        yield temp
        temp += 2
n = int(input())
nums = even(n)
for x in nums:
    print(x, end = ',')