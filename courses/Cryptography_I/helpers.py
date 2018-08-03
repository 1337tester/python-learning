def bin_strings(string):
    return ''.join(format(ord(x), 'b') for x in string)


def hex_to_bin(string):
    """from hex to bin"""
    return bin(int(string, 16))[2:]


def hex_to_int_list(hex_str):
    """converts hexadecimal string into array of integers"""
    return list(int(hex_str[i:i + 2], 16) for i in range(0, len(hex_str), 2))


def ascii_to_int_list(ascii_str):
    """converts ascii string into array of integers"""
    return list(ord(ascii_str[i]) for i in range(0, len(ascii_str)))


def xor_int_lists(list1, list2):
    """xors two lists of integers"""
    return list((i[0] ^ i[1]) for i in zip(list1, list2))


def int_list_to_hex(int_list):
    """converts list of integers into a hex string"""
    result = ''
    for i in int_list:
        if len(hex(i)[2:]) == 1:
            result += '0'
        result += hex(i)[2:]
    return result


def int_to_hex(integer):
    """converts integer into a hex string"""
    result = ''
    if len(hex(integer)[2:]) == 1:
        result += '0'
    result += hex(integer)[2:]
    return result

# a = ascii_to_int_list('aaaa')
# b = hex_to_int_list('aaaaaa')
#
# print(xor_int_lists(a, b))
# print(int_list_to_hex(xor_int_lists(a, b)))


def xor_strings(a, b, base = 'asci'):
    if base =='asci':
        x = int(bin_strings(a), 2)
        y = int(bin_strings(b), 2)
    elif base =='hex':
        x = int(hex_to_bin(a), 2)
        y = int(hex_to_bin(b), 2)
    z = x ^ y
    return bin(z)[2:].zfill(len(a))


def hex_to_chars(hex_data):
    return ''.join(chr(int(hex_data[i:i + 2], 16)) for i in range(0, len(hex_data), 2))






# first = "Pay Bob 100$"
# second = "Pay Bob 500$"
# a = "506179 426f62 35303024"
# b = "506179 426f62 31303024"
# third = "20814804c1767293b99f1d9cab3bc3e7"
#
# prvy_druhy = xor_strings(first, second)
# print(int(prvy_druhy))
# # print(int(bin_strings(prvy_druhy)))
# print(hex_to_bin(third))
