# -*- coding: utf-8 -*-
fi = open("putty.log","r")
fo = open("vysledok.csv","w")

fo.write("cas;cpu;celkova ram;proces maxymo ram")
fo.write("\n")

for line in fi.readlines():
    #cas
    if " up " in line:
       fo.write(line.rsplit(" up ", 1)[0][-8:])
       fo.write(";")   
    #cpu
    elif "Cpu" in line:
        fo.write(line[28:33])
        fo.write(";")
    #celkova pamat ram
    elif "Mem" in line:
        fo.write(line[80:86])
        fo.write(";")
    #proces maxymo ram
    elif "XYmo " in line:
        fo.write(line[36:39])
        fo.write("\n")
   


fi.close()
fo.close()
