from primitive_root import primitive
from typing import Tuple
from genPrime import generate_prime_number
import math

# Initial
p = generate_prime_number(256)
a = generate_prime_number(256)
k = generate_prime_number(256)
alphal = primitive(p)
beta = pow(alphal, a, p)

public_key = (p, alphal, beta)
private_key = (a)

# Encode and Decode
def encode(plaintext: int, k: int):
    y1 = pow(alphal, k, p)
    y2 = ((plaintext % p) * pow(beta, k, p)) % p
    return (y1, y2)

def decode(ciphertext: Tuple[int, int]):
    y1, y2 = ciphertext
    return ((y2 % p) * pow(y1, p - a - 1, p)) % p

# Main
message = input("Enter the 10-base number: ")

while (math.isnan(int(message))):
        message = input("Try again")

plainText = int(message)

cipherText = encode(plainText, k)
print("p:", p)
print("alphal:", alphal)
print("Encode:", cipherText)
print("Decode:", decode(cipherText))

