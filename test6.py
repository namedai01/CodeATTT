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


def sinh():
    p = 7464376294592824421
    pArray = [2, 5, 11, 17, 1544033, 76035503]
    for i in range(1, 10):
        dd = 0
        for j in pArray:
            if module(i, (p-1) // j, p) == 1:
                dd = 1
        if (dd == 0):
            print(i)


# sinh()
# 3 7

p = 7464376294592824421
q = 76035503
t = 40
alpha = module(7, (p-1)//q, p)
print("alpha", alpha) # 4635236418860524607
a = 70000
v = module(alpha, p-a-1, p)
print("v", v) # 1504717096868369242

k = 50000
gammal = module(alpha, k, p)
print("gammal", gammal) # 6133050453575365117

r = 90000
y = (k + a * r) % q
print("y", y) # 65138754

ex1 = ((module(alpha, y, p) % p)*(module(v, r, p))) % p
print("ex1", ex1) # 6133050453575365117
