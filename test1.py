import string, math

p = 1000003
# pArray = [2, 3, 166667]
pArray = [2, 1289]
a = 111111
alpha = 2
k = 2707
sArray = ["NGUY", "ENDU", "CQUO", "CDAI"]

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

beta = module(alpha, a, p)

def sinh(pArray, p):
    for i in range(1, 50):
        dd = 0
        for j in pArray:
            if module(i, (p-1) // j, p) == 1:
                dd = 1
        if (dd == 0):
            print(i)
# print(sinh(pArray, 2579))
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
    
# x = []
# for i in sArray:
#     x.append(any_base_to_dec(i, 26))

# print(x)

# y2 = []
# for i in x:
#     y2.append((i * module(beta, k, p)) % p)

# y1 = module(alpha, k, p)

# print(y1, y2)
# # 197645, [848493, 19919, 370472, 747515]

# d = []
# for i in y2:
#     d.append((i * module(y1, p-a-1, p)) % p)

# print(d)
# #[362021, 413320, 162008, 2308]

# for i in d:
#     print(dec_to_any_base(i, 26))
