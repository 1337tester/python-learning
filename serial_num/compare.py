# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:27:15 2016

@author: Miso
"""
import csv

file1 = open('existing.txt', 'r')
existing_serial = file1.read().splitlines()
all_serial_SIM = []
not_found = []
every_serial = []

with open('myAlert_Global.csv', newline='') as csvfile:
    myAlert_Global = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in myAlert_Global:
        every_serial.append(row[0])
        if row[0] in existing_serial:
            all_serial_SIM.append(row[10])
    for item in existing_serial:
        if item not in every_serial:
            not_found.append(item)

#print(all_serial_SIM)
#print(len(all_serial_SIM))


output = open('ICCID.txt', 'w')
#
for item in all_serial_SIM:
    output.write(item + '\n')

output.close()
file1.close()
csvfile.close()

#
#found = []
#
#for text in comparing_what:
#    if text not in comparing_with:
#        not_found.append(text)
#    else:
##        print('Serial ' + text + ' was found')
#        found.append(text)
        
for line in not_found:
    print(line)