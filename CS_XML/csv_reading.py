import csv

'''with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
'''
with open('names.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')
    print(dir(spamreader))
    print(spamreader.fieldnames)
    print(spamreader.reader)
    '''for row in spamreader:
        print(dir(row))'''

csvfile.close()
