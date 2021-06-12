from libnum.modular import invmod
from libnum.primes import generate_prime
from libnum.sqrtmod import has_sqrtmod_prime_power, sqrtmod_prime_power

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

# calculate modular inverse
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return "Infinity"
        # raise ValueError
    return x % m

class EllipticCurve:
# Constructor
    def __init__(self, a, b, modulo):
        self.a = a
        self.b = b
        self.modulo = modulo
        self.zero = (None, None)

    def is_opposite(self, p1, p2):
        return (p1.x == p2.x and p1.y == -p2.y % self.modulo)

# Given coordinateX, find the coordinateY of the curve.
    def coordinateY(self, coordinateX):
        if (coordinateX < 0 or coordinateX > self.modulo):
            raise ValueError("invalid value of x")
        square_y = self.square_y(coordinateX)
        if not has_sqrtmod_prime_power(square_y, self.modulo):
            return "Invalid"
        y = sqrtmod_prime_power(square_y, self.modulo)
        return list(y)

# Given coordinateX, find the square_coordinateY of the curve.
    def square_y(self, coordinateX):
        return ((coordinateX**3 + self.a * coordinateX + self.b) % self.modulo)

# add function
    def add(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        s = 0
        if (x1 == x2 and y1 == y2):
            temp = modinv(2 * y1, self.modulo)
            if (temp == "Infinity"):
                return "Infinity"
            s = ((3 * (x1 ** 2) + self.a) * temp) % self.modulo
        else:
            temp = modinv(x2 - x1, self.modulo)
            if (temp == "Infinity"):
                return "Infinity"
            s = ((y2 - y1) * temp) % self.modulo
        x3 = (s ** 2 - x1 - x2) % self.modulo
        y3 = (s * (x1 - x3) - y1) % self.modulo
        return (x3, y3)

# double function
    def double(self, p1):
        x1, y1 = p1
        temp = modinv(2 * y1, self.modulo)
        if (temp == "Infinity"):
            return "Infinity"
        s = ((3 * (x1 ** 2) + self.a) * temp) % self.modulo
        x3 = (s ** 2 - x1 - x1) % self.modulo
        y3 = (s * (x1 - x3) - y1) % self.modulo
        return (x3, y3)
# example calc 4*P with P is a point
    def mul(self, generator, multi):
        (x3, y3) = (0, 0)

        (x1, y1) = generator

        (x_tmp, y_tmp) = generator

        init = 0

        for i in str(bin(multi)[2:]):
            if (i == '1') and (init == 0):
                init = 1
            elif (i == '1') and (init == 1):
                exp1 = self.double((x_tmp, y_tmp))
                if (exp1 == "Infinity"):
                    return "Infinity"

                exp2 = self.add((x1, y1), exp1)
                if (exp2 == "Infinity"):
                    return "Infinity"

                (x3, y3) = exp2

                (x_tmp, y_tmp) = (x3, y3)
            else:
                exp = self.double((x_tmp, y_tmp))
                if (exp == "Infinity"):
                    return "Infinity"
                (x3, y3) = exp
                (x_tmp, y_tmp) = (x3, y3)
        return (x3, y3)


# Initial
# p = 938644836833793042910980316283837400364037611289
# a = 1043164860215351
# b = 763682966853749
# s = 774296413624997
# k = 31119936626413
p = 17
a = 2
b = 2
s = 10
k = 14

print(f"Elliptic curve: y^2 = x^3 + {a}*x + {b} mod {p}")

elliptic = EllipticCurve(a, b, p)
pointP = (26039995468231, 821536145248592236470170263794979164517414656707)
# pointP = (5, 1)
pointB = elliptic.mul(pointP, s)

# Encode and Decode
def encode(pointM, k):
    pointM1 = elliptic.mul(pointP, k)
    expM2 = elliptic.mul(pointB, k)
    pointM2 = elliptic.add(pointM, expM2)
    return (pointM1, pointM2)

def decode(pointM1, pointM2):
    exp1 = elliptic.mul(pointM1, s)
    oppExp1 = (exp1[0], p - exp1[1])
    return elliptic.add(oppExp1, pointM2)
    

# Main
# pointM = (16, 4)
pointM = (33722007092201, 481027553862566585110836439308940073566227938415)
pointM1, pointM2 = encode(pointM, k)
print("PlaintCode:", pointM)
print("Encode:", (pointM1, pointM2))
print("Decode:", decode(pointM1, pointM2))
print("kB", elliptic.mul(pointB, k))

