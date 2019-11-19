yearly = 6768
tax_back = 1941
tax_back_total = 0
urok = 1.005
total =0
total_given = 0
years = 30


for i in range(1,years):
    total = (total + yearly) * urok
    total_given += yearly
    tax_back_total += tax_back
    nasporil = str(total + tax_back_total).split('.')[0]
    prid = str(total - total_given + tax_back_total).split('.')[0]
    ekv_urok_num = (((total + tax_back_total)/total_given)**(1/i))*100 - 100
    ekv_urok = "{0:.0f}%".format(ekv_urok_num)
    print('Rok ' + str(i) + ' nasporil: ' + nasporil + ', pridana hodnota: ' + prid + ', urok: ' + ekv_urok)
#    print(ekv_urok)`