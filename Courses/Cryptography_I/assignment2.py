import pyaes
import codecs
import binascii


def xor(var1, var2):
    return bytes(a ^ b for a, b in zip(var1, var2))


def pad(text):
    while len(text) % 8 != 0:
        text += '.'
    return text


def hex_to_chars(hex_data):
    return ''.join(chr(int(hex_data[i:i + 2], 16)) for i in range(0, len(hex_data), 2))


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
##########################################################################3


# CTR
def ctr_decryption(cipher_text, cbc_key, iv_set):
    iv = cipher_text[:32]
    # iv = int.from_bytes(cipher_text[:32], byteorder='big')
    # iv = int.from_bytes(cipher_text[:32], byteorder='big')
    # print(cipher_text[:32], iv)
    cipher_text = cipher_text[32:]
    blocks = []
    while len(cipher_text) > 0:
        blocks.append(cipher_text[:32])
        cipher_text = cipher_text[32:]

    # print('Blocks: ', blocks, type(blocks[0]))
    # print('IV: ', iv)
    # print('Key: ', cbc_key, type(cbc_key))
    results = ''
    for block in blocks:
        # iv = binascii.unhexlify(iv)
        # print('block type', type(block), len(block), block)
        # print('cbc_key type', type(cbc_key), len(cbc_key), cbc_key)
        # print('iv type', type(iv), len(iv), iv)
        aes = pyaes.AESModeOfOperationCBC(binascii.unhexlify(cbc_key))
        function_iv = aes.encrypt(binascii.unhexlify(iv))
        # function_iv = aes.encrypt(binascii.unhexlify(chr(iv)))

        function_iv = binascii.hexlify(function_iv)
        # print(decrypted, binascii.unhexlify(iv))
        # print(len(decrypted), type(decrypted), len(iv), type(iv))
        # print('Decrypted text: ', decrypted, len(decrypted), type(decrypted), int(decrypted, 16))
        # print('iv type: ', iv, type(iv), len(iv), int(iv, 16))
        # print("Decrypted and iv: ", decrypted, iv)

        result = xor(binascii.unhexlify(function_iv), binascii.unhexlify(block))

        result = binascii.hexlify(result)
        # print("Trying   ", hex_to_chars(result))
        results += codecs.decode(result)

        # print(iv, type(iv), int.from_bytes(iv, byteorder='big'))
        # iv_int = int.from_bytes(iv, byteorder='big') + 1
        # print('Integer is: ', iv_int, type(iv_int))
        # iv = str(iv_int).encode()
        iv = iv_set.pop(0)
        # print('Hex iv is: ', hex(iv_int))

    return results, hex_to_chars(results)


cipher_text3 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.encode(
    "ascii")
cbc_key3 = '36f18357be4dbd77f050515c73fcf9f2'.encode("ascii")

#this set is needed because it was horribly slow to implement incrementation of the IV automatically
iv_set3 = ['69dda8455c7dd4254bf353b773304eed',
          '69dda8455c7dd4254bf353b773304eee',
          '69dda8455c7dd4254bf353b773304eef',
          '69dda8455c7dd4254bf353b773304ef0',
          '69dda8455c7dd4254bf353b773304ef1']
cipher_text4 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.encode(
    "ascii")
cbc_key4 = '36f18357be4dbd77f050515c73fcf9f2'.encode("ascii")
iv_set4 = ['770b80259ec33beb2561358a9f2dc618',
          '770b80259ec33beb2561358a9f2dc619',]
print(ctr_decryption(cipher_text3, cbc_key3, iv_set3))
print(ctr_decryption(cipher_text4, cbc_key4, iv_set4))
################################################
