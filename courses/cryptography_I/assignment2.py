import pyaes
import codecs
import binascii
import sys


def xor(var1, var2):
    return bytes(a ^ b for a, b in zip(var1, var2))


def bin_strings(string):
    return ''.join(format(ord(x), 'b') for x in string)


def hex_to_bin(string):
    """from hex to bin"""
    return bin(int(string, 16))[2:]


def xor_strings(a, b, base = 'hex'):
    print("lengths are: ", len(a), len(b))
    if base =='asci':
        x = int(bin_strings(a), 2)
        y = int(bin_strings(b), 2)
    elif base =='hex':
        x = int(hex_to_bin(a), 2)
        y = int(hex_to_bin(b), 2)
    z = x ^ y
    return bin(z)[2:].zfill(len(a))


def pad(text):
    while len(text) % 8 != 0:
        text += '.'
    return text


def hex_to_chars(hex_data):
    return ''.join(chr(int(hex_data[i:i + 2], 16)) for i in range(0, len(hex_data), 2))


def hex_to_int_list(hex_data):
    result = []
    for i in range(0, len(hex_data), 2):
        result.append(int(hex_data[i:i + 2], 16))
    return result


def int_list_to_hex(int_list):
    result = ''
    for i in int_list:
        if len(hex(i)[2:]) == 1:
            result += '0'
        result += hex(i)[2:]
    return result


# CBC
def cbc_decryption(cipher_text, cbc_key):
    iv = cipher_text[:32]
    cipher_text = cipher_text[32:]
    blocks = []
    while len(cipher_text) > 0:
        blocks.append(cipher_text[:32])
        cipher_text = cipher_text[32:]
    results = ''
    for block in blocks:
        aes = pyaes.AESModeOfOperationCBC(binascii.unhexlify(cbc_key))
        decrypted = aes.decrypt(binascii.unhexlify(block))
        decrypted = binascii.hexlify(decrypted)
        result = xor(binascii.unhexlify(decrypted), binascii.unhexlify(iv))
        result = binascii.hexlify(result)
        results += codecs.decode(result)

        iv = block
    return results, hex_to_chars(results)


cipher_text1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.encode(
    "ascii")
cbc_key1 = '140b41b22a29beb4061bda66b6747e14'.encode("ascii")
cipher_text2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.encode(
    "ascii")
cbc_key2 = '140b41b22a29beb4061bda66b6747e14'.encode("ascii")

print(cbc_decryption(cipher_text1, cbc_key1))
print(cbc_decryption(cipher_text2, cbc_key2))


# ajvi = b'4ca00ff4c898d61e1edbf1800618fb28'
# one = b'Basic CBC       '
# two = b'Basic BBB       '
#
# # print(binascii.a2b_hqx(one))
# ajvi_bin = binascii.unhexlify(ajvi)
# one_b = binascii.hexlify(one)
# two_b = binascii.hexlify(two)
# print(ajvi)
# print(one_b)
# print(two_b)
# one_two = int.from_bytes(xor(one_b, two_b), sys.byteorder)
# print(one_two, type(one_two), xor(one_b, two_b))
# print(xor_strings(xor_strings(one_b, two_b), ajvi))
# print(xor(xor(one_b, two_b), ajvi))
# xored = xor(xor(one_b, two_b), ajvi)
#
# iv_better = xored
# cipher_textx = iv_better + '28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.encode(
#     "ascii")
# print(200*'*')
# print(cbc_decryption(cipher_textx, cbc_key1))

##########################################################################3


# CTR
def ctr_decryption(cipher_text, cbc_key):
    iv = cipher_text[:32]
    cipher_text = cipher_text[32:]
    blocks = []
    while len(cipher_text) > 0:
        blocks.append(cipher_text[:32])
        cipher_text = cipher_text[32:]
    results = ''
    for block in blocks:
        aes = pyaes.AESModeOfOperationCBC(binascii.unhexlify(cbc_key))
        function_iv = aes.encrypt(binascii.unhexlify(iv))
        function_iv = binascii.hexlify(function_iv)
        result = xor(binascii.unhexlify(function_iv), binascii.unhexlify(block))
        result = binascii.hexlify(result)
        results += codecs.decode(result)

        # this part of code increments iv by 1
        temp = hex_to_int_list(iv)
        temp[-1] += 1
        iv = int_list_to_hex(temp)

    return results, hex_to_chars(results)


cipher_text3 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.encode(
    "ascii")
cbc_key3 = '36f18357be4dbd77f050515c73fcf9f2'.encode("ascii")

cipher_text4 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.encode(
    "ascii")
cbc_key4 = '36f18357be4dbd77f050515c73fcf9f2'.encode("ascii")
print(ctr_decryption(cipher_text3, cbc_key3))
print(ctr_decryption(cipher_text4, cbc_key4))
################################################
