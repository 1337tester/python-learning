__author__ = 'e1063127'
import time

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

cas = str(time.time())
# print (cas)
newID = 'ZIM' + cas[0:10] + 'aaa'


file1 = 'inbound_pacs_008_PF_MS_CSAG_whitelist.xml'
file2 = 'inbound_pacs_008_PF_MS_CSAG_whitelist_' + newID + '.xml'

orig_file = open(file1, 'r')

orig_text = orig_file.read()
zoznam = {'{MsgId}':newID,
          '{InstrId}':newID,
          '{TxId}':newID}
new_text = replace_all(orig_text, zoznam)


new_file = open(file2, 'w')
new_file.write(new_text)

orig_file.close()
new_file.close()


