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

def check_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

# print(check_prime(16873926547523941523))
print(get_prime_factors(1000002))