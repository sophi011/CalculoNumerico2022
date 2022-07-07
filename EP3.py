

import numpy as np
import EP1
import EP2

def monta_splines(n, L):
    h = L/(n+1) # tamanho de cada intervalo dentro de [0, 1]
    x = [0]*(n+2)
    phi1 = [0]*(n+2)
    phi2 = [0]*(n+2)
    
    for i in range(n+2):  # definição dos valores dos nós
        x[i] = i*h
    #print(x)

    for i in range(1, n+1):  # definição da expressão de phi em função de x
        xi_ant = str(x[i-1])
        xi_pos = str(x[i+1])

        phi1[i] = "(x - " + xi_ant + ")/" + str(h)  # vale de xi-1 até xi
        phi2[i] = "(" + xi_pos + " - x)/" + str(h)  # vale de xi até xi+1
    return x, phi1, phi2
    #(phi1)
    #print(phi2)

def monta_matriz(n, f, L):

    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)
    n_integral = 10  # precisão do cálculo da integral
    x, phi1, phi2 = monta_splines(n, L)

    for i in range(n):
        a[i] = EP2.calculaIntegral(1, 1, 0, 1, phi, n_integral)


def main():
    pass

monta_splines(6, 7)