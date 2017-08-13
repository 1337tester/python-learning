import pylab as plt


mysample = []
mylinear = []
myquadratic = []
mycubic = []
myexpo = []

for i in range(0,30):
    mysample.append(i)
    mylinear.append(i)
    myquadratic.append(i**2)
    mycubic.append(i**3)
    myexpo.append(1.5**i)

#graph of linear versus quadratic growth
plt.figure('lin quad', figsize=(20,20))
plt.clf()
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mysample, mylinear, '-b', label = 'linear', linewidth = 10.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mysample, myquadratic, 'ro', label = 'quadratic', linewidth = 10.0)
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadratic')

#graph of cubic versus exponential growth
plt.figure('cube exp', figsize=(20,20))
plt.clf()
plt.subplot(121)
plt.ylim(0,140000)
plt.plot(mysample, mycubic, ':', label = 'cubic', linewidth = 10.0)
plt.subplot(122)
plt.ylim(0,140000)
plt.plot(mysample, myexpo, '--', label = 'exponential', linewidth = 10.0)
plt.legend(loc = 'upper left')
plt.title('Cubic vs. Exponential')

#graph of cubic versus exponential growth with log scale
plt.figure('cube exp logarithmic', figsize=(20,20))
plt.clf()
plt.yscale('log')
plt.plot(mysample, mycubic, ':', label = 'cubic', linewidth = 10.0)
plt.plot(mysample, myexpo, '--', label = 'exponential', linewidth = 10.0)
plt.legend(loc = 'upper left')
plt.title('Cubic vs. Exponential')
