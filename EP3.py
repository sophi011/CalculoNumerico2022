

import numpy as np
import EP1
import EP2

def monta_splines(n, L):
    h = L/(n+1) # tamanho de cada intervalo dentro de [0, 1]
    x = [0]*(n+2)
    # funcoes da base do espaço que contem a solução procurada
    phi1 = [0]*(n+2)
    phi2 = [0]*(n+2)
    phi11 = [0]*(n+2)  # produto de phi1 por phi1
    phi22 = [0]*(n+2)  # produto de phi2 por phi2
    phi_ij1 = [0]*(n+2)  # produto de phi em i por phi em j de xi-1 até xi
    phi_ij2  =[0]*(n+2)  # produto de phi em i por phi em j de de xi até xi+1
    
    for i in range(n+2):  # definição dos valores dos nós
        x[i] = i*h
    #print(x)

    for i in range(1, n+1):  # definição da expressão de phi em função de x

        phi1[i] = "(x - " + str(x[i-1]) + ")/" + str(h)  # vale de xi-1 até xi
        phi11[i] = "(x**2 - 2*x*" + str(x[i-1]) + " + " + str(x[i-1]) + "**2"
        phi_ij1[i] = "x**2 - x*" + str()
        phi2[i] = "(" + str(x[i+1]) + " - x)/" + str(h)  # vale de xi até xi+1
    return x, phi1, phi2

def monta_matriz(n, f, L):

    a = np.zeros(n)  # diagonal de baixo da matriz tridiagonal do sistema linear
    b = np.zeros(n)  # diagonal principal da matriz tridiagonal do sistema linear
    c = np.zeros(n)  # diagonal de cima da matriz tridiagonal do sistema linear
    d = np.zeros(n)  # vetor do sistema linear
    n_integral = 10  # precisão do cálculo da integral
    xvec, phi1, phi2 = monta_splines(n, L)

    for i in range(1, n, 2):
        x = xvec[i]
        b[i] = EP2.calculaIntegralSimples(0, 1, phi1, n_integral) + EP2.calculaIntegralSimples(0, 1, phi2, n_integral)


def main():
    pass

monta_splines(6, 7)