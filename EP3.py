"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""

import numpy as np
import EP1
import EP2

def calcula_produto_interno(f_1, f_2, a, b):
    g = "("+ f_1 + ")*("+ f_2 + ")"
    n_integral = 10 #precisão do cálculo da integral
    res = EP2.calculaIntegralSimples(a, b, g, n_integral)
    return res

def produto_interno_L(f_1, Derf_1, f_2, Derf_2, k, q, a, b):
    # função que retorna o produto interno de duas funções de Un
    g = "(" + str(k) + "*(" + Derf_1 + ")*(" + Derf_2 + ")) + (" + str(q) + "*(" + f_1 + ")*(" + f_2 + "))"
    n_integral = 10 #precisão do cálculo da integral

    res = EP2.calculaIntegralSimples(a, b, g, n_integral)
    
    return res

def monta_chapeu(n, L, a=0, b=0):
    h = L/(n+1) # tamanho de cada intervalo dentro de [0, L]
    vecx = np.zeros(n+2)

    # funcoes da base do espaço que contem a solução procurada
    phiEsq = ["0"]*(n+2)
    phiDir = ["0"]*(n+2)
    
    for i in range(n+2):  # definição dos valores dos nós
        vecx[i] = i*h

    phiEsq[0] = "(x + " + str(vecx[1]) + ")/" + str(h)
    phiDir[0] = "(" + str(vecx[1]) + " - x)/" + str(h)
    phiEsq[n+1] = "(x - " + str(vecx[n]) + ")/" + str(h)
    phiDir[n+1] = "(" + str(vecx[n+1]+h) + " - x)/" + str(h)

    for i in range(1, n+1):  # definição da expressão de phi em função de x
        phiEsq[i] = "(x - " + str(vecx[i-1]) + ")/" + str(h)  # vale de xi-1 até xi
        phiDir[i] = "(" + str(vecx[i+1]) + " - x)/" + str(h)  # vale de xi até xi+1

    return vecx, h, phiEsq, phiDir

def monta_matriz(n, f, L, k, q, a=0, b=0):

    veca = np.zeros(n)  # diagonal de baixo da matriz tridiagonal do sistema linear
    vecb = np.zeros(n)  # diagonal principal da matriz tridiagonal do sistema linear
    vecc = np.zeros(n)  # diagonal de cima da matriz tridiagonal do sistema linear
    vecd = np.zeros(n)  # vetor do sistema linear
    xvec, h, phiEsq, phiDir = monta_chapeu(n, L)
    
    for i in range(1, n+1):
        x = xvec[i]
        # calcula cada produto interno para formar a matriz tridiagonal
        vecb[i-1] = produto_interno_L(phiEsq[i], "1/"+ str(h), phiEsq[i], "1/"+str(h), k, q, xvec[i-1], xvec[i]) + produto_interno_L(phiDir[i], "(-1)/"+ str(h), phiDir[i], "(-1)/"+str(h), k, q, xvec[i], xvec[i+1])
        vecc[i-1] =  produto_interno_L(phiDir[i], "(-1)/"+ str(h), phiEsq[i+1], "1/"+str(h), k, q, xvec[i], xvec[i+1]) # o único produto nao nulo é entre a descida de phi(xi) com a subida de phi(xi+1)
        vecd[i-1] = calcula_produto_interno(f, phiEsq[i], xvec[i-1], xvec[i]) + calcula_produto_interno(f, phiDir[i], xvec[i], xvec[i+1])

    vecc[n-1] = 0
    for i in range(n-1):    
        veca[i+1] = vecc[i]
        
    print("x: ", xvec)
    print("a: ", veca)
    print("\nb: ", vecb)
    print("\nc: ", vecc)
    print("\nd: ", vecd)
    return veca, vecb, vecc, vecd
    
def validacao(f, n, L, k, q, u, a, b):
    veca, vecb, vecc, vecd = monta_matriz(n, f, L, k, q)
    alphas = EP1.resolve_vetor(veca, vecb, vecc, vecd)  # resolucao considerando condicoes iniciais nulas -- retorna o vetor de alphas
    xvec, h, phiEsq, phiDir = monta_chapeu(n, L)
    u_calc = np.zeros(n)
    u_aprox = np.zeros(n)
    u_real = np.zeros(n)
    for i in range (n):
        x = xvec[i+1]
        u_calc[i] = eval(phiEsq[i+1])*alphas[i] + eval(phiDir[i+1])*alphas[i]
        u_aprox[i] = u_calc[i] + a + (b-a)*x
        u_real[i] = eval(u)
    print("alphas: ", alphas)
    return u_aprox, u_real
    
    
def calcula_erro(u, u_aprox):
    erro_u = np.zeros(len(u))
    for i in range(len(u)):
        erro_u[i] = abs(u_aprox[i] - u[i])
    return max(erro_u)


def main():
    print()
    #f = "12 * x * (1-x) - 2"
    f = "np.exp(x) + 1"
    print("f: ", f)
    #u = "(x**2) * (1-x)**2"
    u = "(x - 1)*(np.exp(-x) - 1)"
    L = 1
    n = 7
    k = "np.exp(x)"
    #k = 1
    print("k: ", k)
    q = 0
    print("q: ", q)
    u_aprox, u_real = validacao(f, n, L, k, q, u, 0, 0)
    print("u_real: ", u_real)
    print("u_aprox: ", u_aprox)
    erro = calcula_erro(u_real, u_aprox)

    print("erro: ", erro)
    print()

if __name__ == "__main__":
    main()
    #print(calcula_produto_interno("x", "x", 1, 0))
    #print(calculaIntegralSimples(0, 1, 'xi**2/2', 6))

#monta_matriz(6, "x", 1)
#monta_chapeu(9, 8)