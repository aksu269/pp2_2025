import math
def filter_prime(a):
    prime = []
    for x in a:
        isPrime = True
        if x <= 1:
            continue
        for i in range (2, int(math.sqrt(x)) + 1):
            if x % i:
                isPrime = False
                break
        if isPrime:
            prime.append(x)
    return prime
a = [2, 7, 11]
print(filter_prime(a))
                