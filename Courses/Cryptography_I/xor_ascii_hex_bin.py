import binascii

def bin_strings(str1):
    return ''.join(format(ord(x), 'b') for x in str1)


def bin_hex(str1):
    return bin(int(str1, 16))[2:]


def xor_strings(a, b, base = 'asci'):
    if base =='asci':
        x = int(bin_strings(a), 2)
        y = int(bin_strings(b), 2)
    elif base =='hex':
        x = int(bin_hex(a), 2)
        y = int(bin_hex(b), 2)
    z = x ^ y
    return bin(z)[2:].zfill(len(a))


# print bin_strings('290b6e3a')

# print(bin_hex('290b6e3a'))
# print(xor_strings('290b6e3a', 'd6f491c5', 'hex'))
# print(xor_strings('5f67abaf', 'bbe033c0', 'hex'))
# print(xor_strings('9d1a4f78', '75e5e3ea', 'hex'))
# print(xor_strings('7b50baab', 'ac343a22', 'hex'))

hex_to_binary = binascii.unhexlify('ac343a22')
print(hex_to_binary)
print(binascii.b2a_uu(hex_to_binary))