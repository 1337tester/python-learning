__author__ = 'e1063127'
import time

def main(file1 = 'inbound_pacs_008_PF_MS_CSAG_whitelist.xml'):
    

    cas = str(time.time())
    newID = 'ZIM' + cas[0:10] + 'aaa' # produces unique ID
    amount = cas[8:13] # random amount
    date = time.strftime('%Y-%m-%d')
    #date = '2016-06-14'  #uncomment to give here any date wished

    file2 = 'inbound_pacs_008_PF_MS_CSAG_whitelist_' + newID + '.xml'
    replacement = {'{MsgId}':newID,
              '{InstrId}':newID,
              '{TxId}':newID,
              '{amount}':amount,
              '{date}':date}

    orig_file = open(file1, 'r')
    orig_text = orig_file.read()
    orig_file.close()

    new_text = replace_all(orig_text, replacement)
    new_file = open(file2, 'w')
    new_file.write(new_text)

    orig_file.close()
    new_file.close()
    
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


if __name__ == "__main__":
    main()

