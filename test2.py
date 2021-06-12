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

def sinh():
    p = 7392616838348633699 
    pArray = [2, 678923759, 5444364511]
    for i in range(1, 10):
        dd = 0
        for j in pArray:
            if module(i, (p-1) // j, p) == 1:
                dd = 1
        if (dd == 0):
            print(i)

def RSA():
    # p1 = 16873926547523941523
    # q1 = 17591732419861160621
    # a1 = 17275767241833392489
    p1 = 1000000007
    q1 = 1000000033
    a1 = 31466456745647
    b1 = gcd_and_inverse((p1-1)*(q1-1), a1)

    n1 = p1 * q1
    print("b1", b1)
    
    a2 = 12764787846358441471
    b2 = 763415006796959133262095430257265686399
    p2 = 48112959837082048697
    q2 = 29497513910652490397
    n2 = q2 * p2
    print("n2 = ", n2)

    s = "DINGUDI"

    x = any_base_to_dec(s, 26)
    print("x = ", x)
    # Ma hoa
    signX = module(x, a1, n1)

    eX = module(x, a2, n2)

    eSignX = module(signX, a2, n2)

    print(signX)

    decrytSignX = module(eSignX, b2, n2)

    print(module(decrytSignX, b1, n1))

    # eSignX = module(signX, a2, n2)

    # eX =  150014665717389868569238623363077448402
    # eSignX =  18895367017168441375221898433098623897

    # Giai ma
    
    # print(dec_to_any_base(module(eX, b1, n1), 26))
    
    # Kiem thu
    # signX = 915024276137878775704995307393586589821

    # eSignX = module(signX, a1, n1)

    # print(eSignX)

    # print(module(eSignX, b1, n1))
    # decrytSignX = module(eSignX, b1, n1)

    # decrytX = dec_to_any_base(module(decrytSignX, b2, n2) , 26)

    # print(decrytSignX)

    # while (len(s) % 4 != 0):
    #     s = s + "Z"
    # sArray = []
    # for i in range(0, len(s)-1, 4):
    #     sArray.append(s[slice(i, i + 4)])

    # x = []
    # for i in sArray:
    #     x.append(any_base_to_dec(i, 26))

    # signX = []
    # eX = [150014665717389868569238623363077448402]
    # for i in x:
    #     signX.append(module(i, a1, n1))
    #     eX.append(module(i, a2, n2))
    
    # eSignX = []
    # for i in signX:
    #     eSignX.append(module(i, a2, n2)) 

    # print(eSignX)

    # GIAI MA
    # decryptX = []
    # for i in eX:
    #     decryptX.append(module(i, b1, n1))

    
    # for i in decryptX:
    #     print(dec_to_any_base(i, 26))
    
    # print(decryptX)

    # KIEM THU
    # for i in eSignX:
    #     temp = module(i, b2, n2)
    #     print(dec_to_any_base(module(temp, b1, n1), 26) )

    # dec_to_any_base(module(module(eSignX, b2, n2), b1, n1), 26)

def elgamal():
    p = 7392616838348633699 
    a = 5053138603308491711
    alpha = 2
    beta = module(alpha, a, p)
    k = 5739350775869162327

    eX = [1225028994138326623, 5341398045818378758]

    dX = ((eX[1] % p) * module(eX[0], p-a-1, p)) % p
    print(dX)

    # s = "OKMAN"

    # x = any_base_to_dec(s, 26)
    
    # gamal = module(alpha, k, p)

    # detal1 = (x - a * gamal) % (p-1) 
    # detal2 = (gcd_and_inverse(p-1, k)[2]) % (p-1)
    # detal = (detal1 * detal2) % (p-1)

    # print(detal)



    # exp1 = module(beta, gamal, p)
    # exp2 = module(gamal, detal, p)
    # expLeft = (exp1 * exp2) % p
    # expRight = module(alpha, x, p)

    # print(gamal, expRight)
    
elgamal()
RSA()





