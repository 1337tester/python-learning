from Crypto.Hash import SHA256


def hashing_per_blocks(filePath = "6.2.birthday.mp4_download", blocksize = 1024):
    file = open(filePath, "rb")
    with file:
        byte = file.read()
        list_of_blocks = []
        while len(byte) > 0:
            list_of_blocks.append(byte[:blocksize])
            byte = byte[blocksize:]
        list_of_blocks = list_of_blocks[::-1]
        hashik = b''
        for block in list_of_blocks:
            h = SHA256.new()
            h.update(block + hashik)
            hashik = h.digest()
        result = h.hexdigest()
    return result

print(hashing_per_blocks("6.1.intro.mp4_download"))