import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from normalize import norm


def func(x, a, b, c):
    return a * np.exp(-b * x) + 2.5


data = np.genfromtxt('./messung1/out.csv', delimiter=',')

ydata25 = np.array(norm(data[2500:4000])[:, 0], np.float32)
ydata10 = np.array(norm(data[2500:4000])[:, 1], np.float32)
xdata = np.array(np.arange(ydata25.shape[0]), np.float32)


plt.figure(1)
plt.subplot(211)

popt25, pcov25 = curve_fit(func, xdata, ydata25)
popt10, pcov10 = curve_fit(func, xdata, ydata10)

plt.plot(ydata25, label='pm2.5')
plt.plot(func(xdata, *popt25), label='pm2.5-regression')
plt.plot(ydata10, label='pm10')
plt.plot(func(xdata, *popt10), label='pm10-regression')

plt.ylabel('linear-scale')
plt.xticks([])

plt.legend()


plt.subplot(212)

popt25, pcov25 = curve_fit(func, xdata, ydata25)
popt10, pcov10 = curve_fit(func, xdata, ydata10)

plt.plot(ydata25, 'o', label='pm2.5', ms=0.5)
plt.plot(ydata10, 'o', label='pm10', ms=0.5)
plt.plot(func(xdata, *popt25), label='pm2.5-regression')
plt.plot(func(xdata, *popt10), label='pm10-regression')

plt.yscale('log')
plt.xticks([])
plt.xlabel('time')
plt.ylabel('log-scale')
plt.show()
