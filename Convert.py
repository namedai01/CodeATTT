import string

def chuyen(s):
    dict_alphabet = dict(zip(string.ascii_uppercase, range(0, 26)))
    newS = ""
    for i in range(0, len(s)):
        newS += str(dict_alphabet[s[i]])
    newS = int(newS)
    return newS


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

# bin(): he 10 -> he 2
# int(string, base): bat ky he nao -> he 10
# oct(): he 10 -> he 8
# hex(): he 10 -> he 16

print(any_base_to_dec("DAI", 26))
print(dec_to_any_base(2036, 26))

