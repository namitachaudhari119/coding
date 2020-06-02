import math

num = 90
prime = 0


def is_prime(x):
    j = 2
    import pdb
    pdb.set_trace()
    while j <= int(math.sqrt(x)):
        if x % j == 0:
            return False
        j += 1
    return True


for i in range(2, num):
    import pdb
    pdb.set_trace()

    if num % i == 0:
        if is_prime(i):
            prime = i

print(prime)
