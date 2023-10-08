import numpy as np
import matplotlib.pyplot as plt

cobre = {'resistividad': 1.68e-8, 'grosor': 1e-3}

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
    return I, B

# N: Número de vueltas
# V: Voltaje
# r: Radio de la bobina o espira
# L = Longitud de la bobina

N = 230
V = 25.37
r = 8.5e-2
L = 28.5e-2

# print(campo_magnetico(cobre, N, V, r, L))