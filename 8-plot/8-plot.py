import matplotlib.pyplot as plt
import numpy as np

data_array = np.loadtxt("data.txt", dtype=int)
data_settings = np.loadtxt("settings.txt", dtype=float)
data_time = np.linspace(0, data_settings[0], data_array.size) * 1000
data_array = data_array * data_settings[1]

fig, ax = plt.subplots()

ax.minorticks_on()
ax.grid(which='major',color='gray',linestyle=':')

ax.plot(data_time, data_array, color='red', linestyle='-', linewidth=0.5, marker='o', markersize=1, markerfacecolor='white', markeredgewidth=2, markeredgecolor='red', markevery=25, label='V(t)')

ax.set_xlim(np.min(data_time), np.max(data_time) + 2)
ax.set_ylim(np.min(data_array), np.max(data_array) + 0.5)

ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

ax.set_title('Процесс заряда и разряда конденсатора в RC цепи')

ax.legend()

ax.grid(True, color='gray', linestyle='-')

ax.legend()
plt.text(8.5,1.25, 'Время заряда: 5.72 сек.')
plt.text(8.5,1.1, 'Время разряда: 7.74 cек.')

fig.savefig("data_grafic.svg")
plt.show()

