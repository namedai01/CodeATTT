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
    n = a
    
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
    if (y2 < 0):
        y2 = y2 + n
    return [d, x2, y2]

# print(gcd_and_inverse(22*28, 127))
def dec_to_any_base(n, base):
    if base == 26:
        alphabet = string.ascii_uppercase
        res = ""
        while (n != 0):     
            res = alphabet[n % 26] + res
            n = n // 26
        return res
    elif base == 2:
        return bin(n)
    elif base == 8:
        return oct(n)
    elif base == 16:
        return hex(n)

def any_base_to_dec(s, base):
    if base == 26:
        dict_alphabet = dict(zip(string.ascii_uppercase, range(0, 26)))
        k = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += base**k * dict_alphabet[s[i]]
            k += 1
        return res
    else:
        return int(s, base)

pArray = [2, 3, 7, 1543, 1543067]

def sinh(pArray, p):
    for i in range(1, 50):
        dd = 0
        for j in pArray:
            if module(i, (p-1) // j, p) == 1:
                dd = 1
        if (dd == 0):
            print(i)



