import matplotlib.pyplot as plt
from bobina import *
voltajes = [1.5, 3, 4.5, 6.5, 7.5, 25.37]
valores_teoricos_corriente = []
valores_experimentales_corriente = [0.6, 1.15, 1.9, 2.14, 2.7, 8]

for i in voltajes:
    valores_teoricos_corriente.append(campo_magnetico(cobre, N, i, r, L)[0])
plt.plot(voltajes,valores_teoricos_corriente,'.-')
plt.plot(voltajes,valores_experimentales_corriente,'.-')
plt.xlabel('Voltaje (V)')
plt.ylabel('Intensidad de corriente eléctrica (A)')
plt.grid()
plt.savefig('I vs V.png')
plt.show()
# print(amperaje)