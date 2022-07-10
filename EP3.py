"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""

import numpy as np
import EP1
import EP2

def calcula_produto_interno(f_1, f_2, a, b):
    # função que calcula o produto interno de duas funções
    g = "("+ f_1 + ")*("+ f_2 + ")"
    n_integral = 10 #precisão do cálculo da integral

    res = EP2.calculaIntegralSimples(a, b, g, n_integral)
    
    return res

def monta_splines(n, L, a=0, b=0):
    h = L/(n+1) # tamanho de cada intervalo dentro de [0, L]
    vecx = [0]*(n+2)

    # funcoes da base do espaço que contem a solução procurada
    phiEsq = ["0"]*(n+2)
    phiDir = ["0"]*(n+2)
    #phiEsqQuad = ["0"]*(n+2)  # produto de phiEsq por phiEsq
    #phiDirQuad = ["0"]*(n+2)  # produto de phiDir por phiDir
    #phi_ijEsq = ["0"]*(n+2)  # produto de phi em i por phi em j de xi-1 até xi
    #phi_ijDir  =["0"]*(n+2)  # produto de phi em i por phi em j de de xi até xi+1
    
    for i in range(n+2):  # definição dos valores dos nós
        vecx[i] = i*h

    phiEsq[0] = "(x + " + str(vecx[1]) + ")/" + str(h)
    phiDir[0] = "(" + str(vecx[1]) + " - x)/" + str(h)
    phiEsq[n+1] = "(x - " + str(vecx[n]) + ")/" + str(h)
    phiDir[n+1] = "(" + str(vecx[n+1]+h) + " - x)/" + str(h)

    for i in range(1, n+1):  # definição da expressão de phi em função de x
        phiEsq[i] = "(x - " + str(vecx[i-1]) + ")/" + str(h)  # vale de xi-1 até xi
        phiDir[i] = "(" + str(vecx[i+1]) + " - x)/" + str(h)  # vale de xi até xi+1
        #phiEsqQuad[i] = "(x**2 - 2*x*" + str(vecx[i-1]) + " + " + str(vecx[i-1]) + "**2)/" + str(h) + "**2"
        #phi_ijEsq[i] = "(x**2 - x*" + str(vecx[i-2]) + " - x*" + str(vecx[i-1]) + " + " + str(vecx[i-1]) + "*" + str(vecx[i-2]) + ")/ "+ str(h) + " **2"
        #phi_ijDir[i] = "(" + str(vecx[i+1]) + "*" + str(vecx[i]) + " -x*" + str(vecx[i]) + " + x**2)/" + str(h) + "**2"
        #phiDirQuad[i] = "(" + phiDir[i] + ")*(" + phiDir[i] + ")"
    #phiDir[0] = a
    #phiDir[n+1] = b

    #phiDirQuad[0] = "(" + phiDir[0] + ")**2"
    print("\n phiEsq: ", phiEsq)
    print("\n phiDir: ", phiDir)
    #print("\n phiEsqQuad: ", phiEsqQuad)
    #print("\n phiDirQuad: ", phiDirQuad)
    #print("\n phi_ijEsq: ", phi_ijEsq)
    #print("\n phi_ijDir: ", phi_ijDir)
    return vecx, phiEsq, phiDir

def monta_matriz(n, f, L, a=0, b=0):

    veca = np.zeros(n)  # diagonal de baixo da matriz tridiagonal do sistema linear
    vecb = np.zeros(n)  # diagonal principal da matriz tridiagonal do sistema linear
    vecc = np.zeros(n)  # diagonal de cima da matriz tridiagonal do sistema linear
    vecd = np.zeros(n)  # vetor do sistema linear
    n_integral = 10  # precisao do calculo da integral
    xvec, phiEsq, phiDir = monta_splines(n, L)
    
    for i in range(1, n+1):
        x = xvec[i]
        # calcula cada produto interno para formar a matriz tridiagonal
        vecb[i-1] = calcula_produto_interno(phiEsq[i], phiEsq[i], xvec[i-1], xvec[i]) + calcula_produto_interno(phiDir[i], phiDir[i], xvec[i], xvec[i+1]) 
        vecc[i-1] = calcula_produto_interno(phiEsq[i+1], phiEsq[i], xvec[i-1], xvec[i]) + calcula_produto_interno(phiDir[i+1], phiDir[i], xvec[i], xvec[i+1])
        vecd[i-1] = calcula_produto_interno(f, phiEsq[i], xvec[i-1], xvec[i]) + calcula_produto_interno(f, phiDir[i], xvec[i], xvec[i+1])

    vecc[n-1] = 0
    for i in range(n-1):    
        veca[i+1] = vecc[i]
        
    print("a: ", veca)
    print("\nb: ", vecb)
    print("\nc: ", vecc)
    print("\nd: ", vecd)
    return veca, vecb, vecc, vecd
    
def validacao(f, n, L, u, a, b):
    veca, vecb, vecc, vecd = monta_matriz(n, f, L)
    alphas = EP1.resolve_vetor(veca, vecb, vecc, vecd)  # resolucao considerando condicoes iniciais nulas -- retorna o vetor de alphas
    xvec, phiEsq, phiDir = monta_splines(n, L)
    u_calc = np.zeros(n)
    u_aprox = np.zeros(n)
    u_real = np.zeros(n)
    for i in range (n):
        x = xvec[i+1]
        u_calc[i] = eval(phiEsq[i+1])*alphas[i] + eval(phiDir[i+1])*alphas[i]
        u_aprox[i] = u_calc[i] + a + (b-a)*x
        u_real[i] = eval(u)

    return u_aprox, u_real
    
    
def calcula_erro(u, u_aprox):
    erro_u = np.zeros(len(u))
    for i in range(len(u)):
        erro_u[i] = abs(u_aprox[i] - u[i])
    return erro_u


def main():
    #f = "12 * x * (1-x) - 2"
    #u = "(x**2) * (1-x)**2"
    #L = 1
    #n = 7
    #u_aprox, u_real = validacao(f, n, L, u, 0, 0)
    #print("u_real: ", u_real)
    #print("u_aprox: ", u_aprox)
    #erro = calcula_erro(u_real, u_aprox)
#
    #print("erro: ", erro)
    print(calcula_produto_interno("x", "x", 0, 1))

if __name__ == "__main__":
    main()
    #print(calculaIntegralSimples(0, 1, 'xi**2/2', 6))

#monta_matriz(6, "x", 1)
#monta_splines(9, 8)