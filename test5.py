def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

# calculate `modular inverse`

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return "Infinity"
        # raise ValueError
    return x % m
# double function

def ecc_double(x1, y1, p, a):
    temp = modinv(2 * y1, p)
    if (temp == "Infinity"):
        return temp
    s = ((3 * (x1 ** 2) + a) * temp) % p
    x3 = (s ** 2 - x1 - x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)

# add function

def ecc_add(x1, y1, x2, y2, p, a):
    s = 0
    if (x1 == x2 and y1 == y2):
        temp = modinv(2 * y1, p)
        if (temp == "Infinity"):
            return temp
        s = ((3 * (x1 ** 2) + a) * temp) % p
    else:
        temp = modinv(x2 - x1, p)
        if (temp == "Infinity"):
            return temp
        s = ((y2 - y1) * temp) % p
    x3 = (s ** 2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


def double_and_add(multi, generator, p, a):
    (x3, y3) = (0, 0)
    (x1, y1) = generator
    (x_tmp, y_tmp) = generator
    init = 0
    for i in str(bin(multi)[2:]):
        if (i == '1') and (init == 0):
            init = 1
        elif (i == '1') and (init == 1):

            exp1 = ecc_double(x_tmp, y_tmp, p, a)

            if (exp1 == "Infinity"):
                return "Infinity"

            (x3, y3) = exp1

            exp2 = ecc_add(x1, y1, x3, y3, p, a)
            if (exp2 == "Infinity"):
                return "Infinity"

            (x3, y3) = exp2

            (x_tmp, y_tmp) = (x3, y3)
        else:
            exp = ecc_double(x_tmp, y_tmp, p, a)
            if (exp == "Infinity"):
                return "Infinity"
            (x3, y3) = exp
            (x_tmp, y_tmp) = (x3, y3)

    return (x3, y3)


def qP(a, b, p):
    array1 = {}
    array2 = {}
    for i in range(1, (p-1) // 2 + 1):
        exp1 = (i ** 2) % p
        exp2 = ((p - i) ** 2) % p
        if (exp1 == exp2):
            array1[exp1] = i
            array2[i] = exp1

    array3 = {}
    for i in range(0, p):
        temp = (i ** 3 + a * i + b) % p
        if (temp in array2.values()):
            # print(array1[temp])
            array3[i] = array1[temp]
            # print(array1[temp])
    
    # for i in array3.keys():
    #     print(i)

    for i in array3.keys():
        genarator = (i, array3[i])
        for j in range(2, p):
            exp = double_and_add(j, genarator, p, a)
            if (exp == "Infinity"):
                print(j)
                break

a = 1
b = 1
p = 3

qP(a, b, p)

# print("diem", (10, 10), "Cap", 1)
print(double_and_add(2, (4, 1), 7, 1))

