import math

def get_prime_factors(number):
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
            
    if number > 2:
        prime_factors.append(int(number))

    return prime_factors

def primitive(p):
    pArray = get_prime_factors(p - 1)
    i = 1
    while (i >= 1):
        dd = 0
        i = i + 1
        for j in pArray:
            if pow(i, (p - 1) // j, p) == 1:
                dd = 1
        if (dd == 0):
            return i

# print(primitive(761))
