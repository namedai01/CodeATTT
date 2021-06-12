# y2 = b^-1
# b^-1 mod a
# ax + by = d = gcd(a, b)
# d = a
# x = x2, y = y2

def gcd_and_inverse(a, b):
    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0
    
    while b > 0:
        q = a // b
        r = a % b
        a = b
        b = r
        x = x2 - q * x1
        y = y2 - q * y1
        x2 = x1
        y2 = y1
        x1 = x
        y1 = y
    d = a    
    return [d, x2, y2]
# bin(): he 10 -> he 2
# int(): bat ky he nao -> he 10
# oct(): he 10 -> he 8
# hex(): he 10 -> he 16

# b^-1 mod a => y2 = b^-1
import string

def module(b, n, m):
    n = bin(n)
    n = n[2:]
    n = n[::-1]
    x = 1
    power = b % m
    for i in range(0, len(n)):
        if (n[i] == str(1)):
            x = (x * power) % m
        power = (power ** 2) % m
    return x

print(module(2, 1999, 2579))

# dict_alphabet = dict(zip(range(0, 26), string.ascii_uppercase))

# def get_key(val):
#     for key, value in dict_alphabet.items():
#         if val == value:
#             return key
#     return "key doesn't exist"



