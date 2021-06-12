import math


def check_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


def ExtendedEuclide(a, b):
    if(b == 0):
        return 1
    else:
        d = a
        x2 = 1
        x1 = 0
        y1 = 1
        y2 = 0
        while(b > 0):
            q = a//b
            r = a % b
            x = x2 - q * x1
            y = y2 - q * y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
        if(y2 < 0):
            y2 += d
        return y2


def pollard(n):
    B = 29
    a = 3
    d = gcd(a, n)
    if(d >= 2):
        return d
    for q in range(B + 1):
        if(check_prime(q)):
            l = math.log(n) // math.log(q)
            a = a**(q**l) % n
    d = gcd(a - 1, n)
    if(d > 1 and d < n):
        return d
    return "Error Algorithm"

def privitiveElement(p):
    # mac dinh p - 1 = p
    primes = []
    foo = p
    for i in range(2, p):
        check = False
        while(foo % i == 0):
            check = True
            foo /= i
        if(check):
            primes.append(i)
    privitive = []
    for i in range(2, p):
        check = True
        for prime in primes:
            bar = p // prime
            if(i**bar % (p + 1) == 1):
                check = False
                break
        if(check):
            privitive.append(i)
        if(len(privitive) == 1):
            return privitive
    return privitive


def so_hoa_ten(name, base=26):
    name = name.lower()
    len_name = len(name)
    i = 1
    ord_a = ord('a')
    ans = 0
    for char in name:
        new_char_code = ord(char)-ord_a
        offset = len_name - i
        ans += new_char_code*base**offset
        i += 1
    return ans

print(so_hoa_ten("TRIN"))

def binary_reverse(n):
    ans = []
    while(n > 0):
        if(n % 2 == 0):
            ans.append(0)
        else:
            ans.append(1)
        n = n // 2
    return ans


def modularExponentiation(b, n, m):
    # b^n mod m
    a = binary_reverse(n)
    x = 1
    power = b % m
    for i in range(len(a)):
        if(a[i] == 1):
            x = (x * power) % m
        power = (power*power) % m
    return x


def ElGamal(p, k, a, alpha, name):
    beta = modularExponentiation(alpha, a, p)
    x = so_hoa_ten(name)
    y1 = modularExponentiation(alpha, k, p)
    y2 = (x * modularExponentiation(beta, k, p)) % p
    print(y1, y2)


if __name__ == "__main__":
    p = 1000003
    alpha = 5
    a = 122843
    k = 201
    name = 'trin'
    beta = 995374
    x = 345657

    # print(ExtendedEuclide(12210*12346, a))
    # print(check_prime(b))
    # print(check_prime(a))
    # print(gcd(12346*12210,a ))
    # print(modularExponentiation(7,39,71))
    # print(modularExponentiation(11,43,71))
    #
    # print(modularExponentiation(5362312, 11975151, 150769217))
    # print(check_prime(p))
    # print(modularExponentiation(alpha, a, p))
    # print(so_hoa_ten(name))
    # ElGamal(p, k, a, alpha, name)
    # print(modularExponentiation(658165, (p - a - 1), p))
