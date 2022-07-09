"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""

import numpy as np
import EP1
import EP2

def monta_splines(n, L, a=0, b=0):
    h = L/(n+1) # tamanho de cada intervalo dentro de [0, 1]
    vecx = [0]*(n+2)
    # funcoes da base do espaço que contem a solução procurada
    phiEsq = ["0"]*(n+2)
    phiDir = ["0"]*(n+2)
    phiEsqQuad = ["0"]*(n+2)  # produto de phiEsq por phiEsq
    phiDirQuad = ["0"]*(n+2)  # produto de phiDir por phiDir
    phi_ijEsq = ["0"]*(n+2)  # produto de phi em i por phi em j de xi-1 até xi
    phi_ijDir  =["0"]*(n+2)  # produto de phi em i por phi em j de de xi até xi+1
    
    for i in range(n+2):  # definição dos valores dos nós
        vecx[i] = i*h
    #print(x)

    for i in range(1, n+1):  # definição da expressão de phi em função de x

        phiEsq[i] = "(x - " + str(vecx[i-1]) + ")/" + str(h)  # vale de xi-1 até xi
        phiEsqQuad[i] = "(x**2 - 2*x*" + str(vecx[i-1]) + " + " + str(vecx[i-1]) + "**2)/" + str(h) + "**2"
        phi_ijEsq[i] = "(x**2 - x*" + str(vecx[i-2]) + " - x*" + str(vecx[i-1]) + " + " + str(vecx[i-1]) + "*" + str(vecx[i-2]) + ")/ "+ str(h) + " **2"
        phi_ijDir[i] = "(" + str(vecx[i+1]) + "*" + str(vecx[i]) + " -x*" + str(vecx[i]) + " + x**2)/" + str(h) + "**2"
        phiDir[i] = "(" + str(vecx[i+1]) + " - x)/" + str(h)  # vale de xi até xi+1
        phiDirQuad[i] = "(" + phiDir[i] + ")*(" + phiDir[i] + ")"
    phiDir[0] = a
    phiDir[n+1] = b

    phiDirQuad[0] = "(" + phiDir[0] + ")**2"
    print("\n phiEsq: ", phiEsq)
    print("\n phiDir: ", phiDir)
    print("\n phiEsqQuad: ", phiEsqQuad)
    print("\n phiDirQuad: ", phiDirQuad)
    print("\n phi_ijEsq: ", phi_ijEsq)
    print("\n phi_ijDir: ", phi_ijDir)
    return vecx, phiEsq, phiDir, phiEsqQuad, phiDirQuad, phi_ijEsq, phi_ijDir

def monta_matriz(n, f, L, a=0, b=0):

    veca = np.zeros(n)  # diagonal de baixo da matriz tridiagonal do sistema linear
    vecb = np.zeros(n)  # diagonal principal da matriz tridiagonal do sistema linear
    vecc = np.zeros(n)  # diagonal de cima da matriz tridiagonal do sistema linear
    vecd = np.zeros(n)  # vetor do sistema linear
    n_integral = 10  # precisao do calculo da integral
    xvec, phiEsq, phiDir, phiEsqQuad, phiDirQuad, phi_ijEsq, phi_ijDir = monta_splines(n, L, "1", "1")
    
    for i in range(n):
        x = xvec[i]
        gEsq = "("+ f + ")*("+ str(phiEsq[i]) + ")"
        gDir = "("+ f + ")*("+ str(phiDir[i]) + ")"
        #print(type(phiEsqQuad[i]))
        vecb[i] = EP2.calculaIntegralSimples(0, 1, phiEsqQuad[i], n_integral) + EP2.calculaIntegralSimples(0, 1, phiDirQuad[i], n_integral)
        veca[i] = EP2.calculaIntegralSimples(0, 1, phi_ijEsq[i], n_integral) + EP2.calculaIntegralSimples(0, 1, phi_ijDir[i], n_integral)
        vecd[i] = EP2.calculaIntegralSimples(0, 1, gEsq, n_integral) + EP2.calculaIntegralSimples(0, 1, gDir, n_integral)
    for i in range(n-1):    
        vecc[i] = veca[i+1]
        
    #print("a: ", a)
    #print("\nb: ", b)
    #print("\nc: ", c)
    #print("\nd: ", d)
    return veca, vecb, vecc, vecd
    
def validacao(f, n, L, a, b):
    veca, vecb, c, d = monta_matriz(n, f, L)
    alphas = EP1.resolve_vetor(a, b, c, d)  # resolucao considerando condicoes iniciais nulas -- retorna o vetor de alphas
    

def main():
    pass

monta_matriz(6, "x", 1)
#monta_splines(6, 1)