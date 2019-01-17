import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from normalize import norm

data = np.genfromtxt('./sylvester/out.csv', delimiter=',')
data = norm(data)


pm25 = list(data[:,0])
pm10 = list(data[:,1])


plt.scatter(pm25, pm10, c=np.arange(len(pm10)), cmap='gnuplot', s=0.1)
cbar = plt.colorbar()
ticks = ['16:00', '18:00', '20:00', '22:00', '24:00', '02:00']

cbar.set_ticks(range(len(pm10))[::60*60*2])
#cbar.set_label('time in sconds')

cbar.ax.set_yticklabels(ticks)

plt.xlabel('pm2.5 in µg/m³')
plt.ylabel('pm10 in µg/m³')

plt.show()
