import numpy as np
import matplotlib.pyplot as plt

# corriente = [valor1, valor2, valor3]


cobre = {'resistividad': 1, 'grosor': 1e-3}



def campo_magnetico(material, N, V, r, L):
    mu_0 = 4*np.pi*1e-7
    grosor = material['grosor']
    At = np.pi*(grosor/2)**2
    Le = 2*np.pi*r
    Lb = Le*N
    rho = material['resistividad']
    R = rho*Lb/At
    I = V/R
    B = mu_0*I*N/L
    return B

# N: Número de vueltas
# V: Voltaje
# r: Radio de la bobina o espira
# L = Longitud de la bobina

N = 250
V = 3
r = 10e-2
L = 30e-2
print(campo_magnetico(cobre, N, V, r, L))