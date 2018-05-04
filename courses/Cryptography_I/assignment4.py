import urllib.request, urllib.error, urllib.parse
from helpers import xor_int_lists, int_to_hex, int_list_to_hex

TARGET = 'http://crypto-class.appspot.com/po?er='


# --------------------------------------------------------------
# padding oracle
# --------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib.parse.quote(q)  # Create query URL
        req = urllib.request.Request(target)  # Send HTTP request to server
        try:
            f = urllib.request.urlopen(req)  # Wait for response
        except urllib.error.HTTPError as e:
            print("We got: %d" % e.code, " ", end='')  # Print response code
            if e.code == 404:
                # print(q)
                return True  # good padding
            return False  # bad padding


def xor_int_lists(list1, list2):
    """xors two lists of integers"""
    return list((i[0] ^ i[1]) for i in zip(list1, list2))


if __name__ == "__main__":
    po = PaddingOracle()
    # po.query(sys.argv[1])       # Issue HTTP query with the given argument
    first_query = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    trial_query = first_query[:-32]
    endof_query = first_query[-32:]
    correct_hex = ''
    pad_num = 1
    guess_list = []
    xor_list = []
    while len(trial_query) > 0:
        well_form_pad = []
        result = False
        guess = 0
        guess_list.insert(0, guess)
        for i in range(pad_num):
            well_form_pad.append(pad_num)
        xor_this = trial_query[-2:]
        xor_list.insert(0, int(trial_query[-2:], 16))
        trial_query = trial_query[:-2]
        while not result:
            guess_list[0] = guess
            # print('xor this: ', xor_this)
            # print('xor this int: ', int(xor_this, 16))
            # print(int(xor_this, 16), guess, 1)
            # print(xor_list, guess_list, well_form_pad)
            guess_xoreda = xor_int_lists(xor_int_lists(xor_list, guess_list), well_form_pad)
            # print(guess_xoreda)
            guess_xored = int(xor_this, 16) ^ guess ^ 1
            # print(trial_query + int_to_hex(guess_xored) + endof_query)
            trying = trial_query + int_list_to_hex(guess_xoreda) + endof_query
            result = po.query(trying)
            print('debug ', trial_query, ' ', int_list_to_hex(guess_xoreda) , end = '')
            print(guess, " ->>> ", result)
            guess += 1
            if guess > 255:
                break
        # endof_query = xor_this + endof_query
        correct_hex = int_to_hex(guess-1) + correct_hex
        guess_list[0] = guess - 1
        print('gues list', guess_list)
        print('correct hex', correct_hex)
        print('well formed pad', well_form_pad)
        pad_num += 1
    print(correct_hex)
