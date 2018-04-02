"""
Implementation of a SHA256 for hashing and verification in 1 Kb blocks. This enables possible launch of verified blocks before the whole file is verified - basis for streaming for example.

Installation:
Copy the 'block_hash.py' to your computer
launch it with 'python3 block_hash.py' (you must have python 3.x installed)
Follow instructions

Disclaimer:
this program was never meant for serious use, I wanted a MVP for my own training, use therefore with caution
provides only resistance against random data loss by design, does not protect against existential forgery
"""
from Crypto.Hash import SHA256


def hashing_per_blocks(filepath, blocksize = 1024):
    """"
    - hashes the file per 1024 bytes blocks starting with the last block
    - creates an additional file where each block is appended the hash of the next block,
        enabling the structural verification per chunks (1024 bytes), instead of
        needing to verify the whole file at once
    - output is the final hash of (first block + hash of the second block)
        + name of the newly created file with hashes implemented
    """
    file = open(filepath, "rb")
    with file:
        byte = file.read()
        list_of_blocks = []
        while len(byte) > 0:
            list_of_blocks.append(byte[:blocksize])
            byte = byte[blocksize:]
        list_of_blocks = list_of_blocks[::-1]
        hashik = b''
        hashed_file_blocks = []
        for block in list_of_blocks:
            h = SHA256.new()
            hashed_file_blocks.append(block + hashik)
            h.update(block + hashik)

            # more congruent solution
            # hashik = str.encode(h.hexdigest())

            # solution for the coursera exercise
            hashik = h.digest()
            # print(type(hashik), hashik, h.hexdigest())
        result = h.hexdigest()
    new_filepath = filepath + '_hashed'
    hashed_file = open(new_filepath, "w+b")
    with hashed_file:
        for block in hashed_file_blocks[::-1]:
            hashed_file.write(block)
            # print(block)
    return result, new_filepath


def verify_per_blocks(filepath, hash0, blocksize = 1024, hashsize = 32):
    """"
    - input is the filepath of the file with injected block hashes and the hash0, blocksize and hashsize should not be edited
    - output is the block by block verification of integrity (exiting in case of first False)
    """
    hashed_file = open(filepath, "rb")
    with hashed_file:
        byte = hashed_file.read()
        list_of_blocks = []
        if type(hash0) == str:
            hashik = byte.fromhex(hash0)
        counter = 0
        while len(byte) > 0:
            block = byte[:blocksize + hashsize]
            h = SHA256.new()
            h.update(block)
            hash_computed = h.digest()

            # old code in case hash0 conversion to byte would not work
            # hash_computed = h.hexdigest()
            # if type(hashik) == bytes:
            #     hash_computed = h.digest()

            correct_blocks = []
            if hashik == hash_computed:
                correct_blocks.append(counter)
                print('Block {} integrity is correct'.format(counter))
            else:
                print('Block {} integrity is incorrect, exiting'.format(counter))
                return False
            counter += 1
            hashik = byte[blocksize:blocksize + hashsize]
            byte = byte[blocksize + hashsize:]
    return print('All blocks are correct')


if __name__ == '__main__':
    hash_or_verify = input("For block-hashing a file press 'h' \nFor veryfying press 'v'\nInput:")
    if hash_or_verify == 'h':
        path = input("Please provide filepath for the hash candidate (best in quotation marks): ")
        print("Working...")
        hash, hashed_file_loc = hashing_per_blocks(path)
        print('Final hash tag for {} is: \n'.format(path), hash)
        print('Hashed file was created as {} in the same directory as original file'.format(hashed_file_loc))
    elif hash_or_verify == 'v':
        path = input("Please provide filepath for the block-hash file (best in quotation marks): ")
        hash = input("Please provide the hash0(hash of the first block of this file): ")
        verify_per_blocks(path, hash)
    else:
        print("Incorrect input")


    #debugging, dont look here;)
    # hash, hashed_file_loc = hashing_per_blocks('6.2.birthday.mp4_download')
    # verify_per_blocks('/home/1337Tester/Dropbox/pyfund/Courses/Cryptography_I/6.2.birthday.mp4_download_hashed', '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8')
    # hash, hashed_file_loc = hashing_per_blocks('notes.txt')
    # # check for notes.txt
    # print(hash == "af98fc9bbfa4c37ad2a4fd877ca3e0738a3433e2f9a86662037254a4f8a3a0d8")
    # verify_per_blocks('/home/1337Tester/Dropbox/pyfund/Courses/Cryptography_I/notes.txt_hashed', 'af98fc9bbfa4c37ad2a4fd877ca3e0738a3433e2f9a86662037254a4f8a3a0d8')
