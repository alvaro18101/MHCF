import matplotlib.pyplot as plt
from bobina import *
voltajes = [1.5, 3, 4.5, 6.5, 7.5, 25.37]
amperaje = []
valores_experimentales = [0.6, 1.15, 1.9, 2.14, 2.7, 8]

for i in voltajes:
    amperaje.append(campo_magnetico(cobre, N, i, r, L)[0])
plt.plot(voltajes,amperaje,'.-')
plt.plot(voltajes,valores_experimentales,'.-')
plt.xlabel('Voltaje (V)')
plt.ylabel('Intensidad de corriente eléctrica (A)')
plt.grid()
plt.savefig('I vs V.png')
plt.show()
# print(amperaje)