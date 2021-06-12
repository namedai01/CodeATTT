from genPrime import generate_prime_number
import math

# Initial
p = generate_prime_number(512)
q = generate_prime_number(512)
e = generate_prime_number(512)

n = p * q
phiN = (p - 1) * (q - 1)
d = pow(e, -1, phiN)

public_key = (n, e)
private_key = (d)

# Encode and decode
def encode(plainText):
    return pow(plainText, e, n)

def decode(ciphertext):
    return pow(ciphertext, d, n)

# Main
message = input("Enter the 10-base number: ")

while (math.isnan(int(message))):
        message = input("Try again")

plainText = int(message)

cipherText = encode(plainText)
print("Encode:", cipherText)
print("Decode:", decode(cipherText))


