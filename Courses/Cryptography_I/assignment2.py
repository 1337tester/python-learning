from Crypto.Cipher import AES
import codecs

def xor1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


def pad(text):
    while len(text) % 8 != 0:
        text += '.'
    return text

cbc_key =               '140b41b22a29beb4061bda66b6747e14'.encode("utf-8")
iv =                    '4ca00ff4c898d61e1edbf1800618fb28'.encode("utf-8")
cbc_ciphertext1_1 =     '28a226d160dad07883d04e008a7897ee'.encode("utf-8")
cbc_ciphertext1_2 =     '2e4b7465d5290d0c0e6c6822236e1daa'.encode("utf-8")
cbc_ciphertext1_3 =     'fb94ffe0c5da05d9476be028ad7c1d81'.encode("utf-8")
whole_cipher1 = '28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

test_text = 'ahoj'#.encode("latin-1")
padded_text = pad(test_text)#.encode("latin-1")


# iv = Random.new().read(AES.block_size)

aes = AES.new(cbc_key, AES.MODE_CBC)

encrypted = aes.encrypt(cbc_ciphertext1_1)

print('Encrypted text: ', encrypted, len(encrypted))
for a in encrypted:
    print(a)
decoded_iv = codecs.decode(iv, 'hex_codec')
print('decoded iv(hex codec): ', decoded_iv, len(decoded_iv))
for a in decoded_iv:
    print(a)
# print('decoded iv: ', iv.decode('ascii'))

# for a in encrypted:
#     print(a)
    # encrypted_decoded += ord(a)
# print("".join(map(chr, encrypted)))
# print(codecs.encode(encrypted, 'hex'))

# str_ggg = ''.join(format(ord(x), 'b') for x in encrypted)
# print(str_ggg)
# print(aes.decrypt(cbc_ciphertext1))




