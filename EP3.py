"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""

import numpy as np
import EP1
import EP2

def produto_interno_d(f_1, f_2, a, b):
    # função que retorna o produto interno de f e phi
    g = "("+ f_1 + ")*("+ f_2 + ")"

    n_integral = 10 #precisão do cálculo da integral

    # resolve a integral com a função criada no EP2
    res = EP2.calculaIntegralSimples(a, b, g, n_integral)

    return res

def produto_interno_L(f_1, Derf_1, f_2, Derf_2, k, q, a, b):
    # função que retorna o produto interno de duas funções de Un
    g = "(" + str(k) + "*(" + Derf_1 + ")*(" + Derf_2 + ")) + (" + str(q) + "*(" + f_1 + ")*(" + f_2 + "))"
    
    n_integral = 10 #precisão do cálculo da integral

    # resolve a integral com a função criada no EP2
    res = EP2.calculaIntegralSimples(a, b, g, n_integral)
    
    return res

def monta_chapeu(n, L, a=0, b=0):
    
    # encontrar os intervalos do nós dentro de [0, L]
    h = L/(n+1)

    # definição dos nós a partir do intervalo definido anteriormente
    vecx = np.zeros(n+2)
    for i in range(n+2):
        vecx[i] = i*h

    # funcoes da base do espaço que contem a solução procurada
    phiEsq = ["0"]*(n+2)
    phiDir = ["0"]*(n+2)

    # condições nos extremos da função phi
    phiEsq[0] = "(x + " + str(vecx[1]) + ")/" + str(h)
    phiDir[0] = "(" + str(vecx[1]) + " - x)/" + str(h)
    phiEsq[n+1] = "(x - " + str(vecx[n]) + ")/" + str(h)
    phiDir[n+1] = "(" + str(vecx[n+1]+h) + " - x)/" + str(h)

    # definição da expressão de phi em função de x
    for i in range(1, n+1):  
        phiEsq[i] = "(x - " + str(vecx[i-1]) + ")/" + str(h)  # vale de xi-1 até xi
        phiDir[i] = "(" + str(vecx[i+1]) + " - x)/" + str(h)  # vale de xi até xi+1

    return vecx, h, phiEsq, phiDir

def monta_matriz(n, f, L, k, q, a=0, b=0):

    # criação dos vetores que caracterizam a matriz tridiagonal do sistema linear
    veca = np.zeros(n)
    vecb = np.zeros(n)  
    vecc = np.zeros(n)  
    vecd = np.zeros(n)  

    # monta a função base para resolução do problema
    xvec, h, phiEsq, phiDir = monta_chapeu(n, L)
    
    # cálculo do produto interno de cada termo da matriz tridiagonal
    for i in range(1, n+1):
        x = xvec[i]
        vecb[i-1] = produto_interno_L(phiEsq[i], "1/"+ str(h), phiEsq[i], "1/"+str(h), k, q, xvec[i-1], xvec[i]) + produto_interno_L(phiDir[i], "(-1)/"+ str(h), phiDir[i], "(-1)/"+str(h), k, q, xvec[i], xvec[i+1])
        vecc[i-1] =  produto_interno_L(phiDir[i], "(-1)/"+ str(h), phiEsq[i+1], "1/"+str(h), k, q, xvec[i], xvec[i+1]) # o único produto nao nulo é entre a descida de phi(xi) com a subida de phi(xi+1)
        vecd[i-1] = produto_interno_d(f, phiEsq[i], xvec[i-1], xvec[i]) + produto_interno_d(f, phiDir[i], xvec[i], xvec[i+1])

    # o produto interno de phi1 com phi2 é igual ao produto interno de phi2 com phi1
    vecc[n-1] = 0
    for i in range(n-1):    
        veca[i+1] = vecc[i]
        
    #print("x: ", xvec)
    #print("\na: ", veca)
    #print("\nb: ", vecb)
    #print("\nc: ", vecc)
    #print("\nd: ", vecd)
    return veca, vecb, vecc, vecd
    
def validacao(f, n, L, k, q, u, a, b):
    # implementação do método dos elementos finitos
    veca, vecb, vecc, vecd = monta_matriz(n, f, L, k, q)

    # resolve a matriz tridiagonal criada
    alphas = EP1.resolve_vetor(veca, vecb, vecc, vecd)
    xvec, h, phiEsq, phiDir = monta_chapeu(n, L)

    # função que aproxima de u
    u_aprox = np.zeros(n)

    # função que se desejava aproximar
    u_real = np.zeros(n)

    # definição dos valores de u_real e u_aprox
    for i in range (n):
        x = xvec[i+1]
        #u_calc[i] = eval(phiEsq[i+1])*alphas[i] + eval(phiDir[i+1])*alphas[i]
        #u_aprox[i] = u_calc[i] + a + (b-a)*x

        u_aprox[i] = alphas[i] + a + (b-a)*x
        u_real[i] = eval(u)

    return u_aprox, u_real, xvec
    
    
def calcula_erro(u, u_aprox):
    # função que retorna o maior erro de aproximação da função
    erro_u = np.zeros(len(u))
    for i in range(len(u)):
        erro_u[i] = abs(u_aprox[i] - u[i])

    return max(erro_u)

def calcula_exemplo1(n):
    f = "12 * x * (1-x) - 2"
    u = "(x**2) * (1-x)**2"
    L = 1
    k = 1
    q = 0
    u_aprox, u_real, xvec = validacao(f, n, L, k, q, u, 0, 0)
    erro = calcula_erro(u_real, u_aprox)
    #print("\nn: ", n)
    #print("\nf: ", f)
    #print("\nk: ", k)
    #print("\nq: ", q)
    #print("\nL: ", L)
    print("\nu_real: ", u_real)
    print("\nu_aprox: ", u_aprox)
    print("\nerro: ", erro)

def calcula_exemplo_complementar(n):
    f = "np.exp(x) + 1"
    u = "(x - 1)*(np.exp(-x) - 1)"
    L = 1
    k = "np.exp(x)"
    q = 0
    u_aprox, u_real, xvec = validacao(f, n, L, k, q, u, 0, 0)
    erro = calcula_erro(u_real, u_aprox)
    #print("n: ", n)
    #print("f: ", f)
    #print("k: ", k)
    #print("q: ", q)
    #print("L: ", L)
    print("\nu_real: ", u_real)
    print("\nu_aprox: ", u_aprox)
    print("\nerro:", erro)
    print("\n\n\n\n")

def calcula_calor_gaussiana(q0pos, q0neg, L, sigma, theta, n):
    q_pos = str(q0pos) + "*np.exp(-(x-" + str(L) + "/2)**2/(" + str(sigma) + "**2))"
    q_neg = str(q0neg) + "*(np.exp(-(x**2)/" + str(theta) + "**2) + np.exp(-(x-" + str(L) + ")**2/(" + str(theta) + "**2)))"
    Q = q_pos + " - " + q_neg
    k = 3.6
    q = 0
    u = "0"
    u_aprox, u_real, xvec = validacao(Q, n, L, k, q, u, 0, 0)
    print("u_aprox: ", u_aprox)
    for i in range(len(u_aprox)):   
        comp = 1000*xvec[i]
        temp = u_aprox[i] + 273
        x = xvec[i]
        print("qpos = ", eval(q_pos))
        print("em x = %.2f mm a temperatura é %d °C" %(comp, temp))
    return u_aprox

def calcula_mudanca_material(n, ks, ka):
    # @TODO
    pass

def main():
    print("\n\n\n------ VALIDAÇÃO ------")
    print("\n\nPara n = 7")
    calcula_exemplo1(7)

    print("\n\n\n------ VALIDAÇÃO ------")
    print("\n\nPara n = 15")
    calcula_exemplo1(15)

    print("\n\n\n------ VALIDAÇÃO ------")
    print("\n\nPara n = 31")
    calcula_exemplo1(31)

    print("\n\n\n------ VALIDAÇÃO ------")
    print("\n\nPara n = 63")
    calcula_exemplo1(63)

    print("\n\n\n------ EXEMPLO COMPLEMENTAR ------")
    print("\n\nPara n = 7")
    calcula_exemplo_complementar(7)

    print("\n\n\n------ EXEMPLO COMPLEMENTAR ------")
    print("\n\nPara n = 15")
    calcula_exemplo_complementar(15)

    print("\n\n\n------ EXEMPLO COMPLEMENTAR ------")
    print("\n\nPara n = 31")
    calcula_exemplo_complementar(31)

    print("\n\n\n------ EXEMPLO COMPLEMENTAR ------")
    print("\n\nPara n = 63")
    calcula_exemplo_complementar(63)
    #calcula_exemplo_complementar(31)
    #print("------ EXEMPLO CALOR GERADO COM FUNÇÃO GAUSSIANA ------")
    #calcula_calor_gaussiana(750000, 10000, 0.02, 1, 1, 7)


if __name__ == "__main__":
    main()
