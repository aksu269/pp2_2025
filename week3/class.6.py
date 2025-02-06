import math
def myfunc(x):
    if x <= 1:
        return False
    else:
        for i in range (2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
    return True
numbers = [1, 3, 5, 6]
prime_numbers = list(filter(lambda x: myfunc(x), numbers))
print(prime_numbers)