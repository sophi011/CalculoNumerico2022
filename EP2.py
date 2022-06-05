"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""
import math
import numpy as np

def no_peso(n):
    # x[j] = -x[j] <-> w[j]
    if n == 6:
        x = np.array([-0.9324695142031520278123016, -0.6612093864662645136613996, -0.2386191860831969086305017, 0, 0.2386191860831969086305017, 0.6612093864662645136613996, 0.9324695142031520278123016])
        w = np.array([0.1713244923791703450402961 , 0.3607615730481386075698335, 0.4679139345726910473898703, 0, 0.4679139345726910473898703, 0.3607615730481386075698335, 0.1713244923791703450402961])
    elif n == 8:
        x = np.array([-0.9602898564975362316835609, -0.7966664774136267395915539, -0.5255324099163289858177390, -0.1834346424956498049394761, 0, 0.1834346424956498049394761, 0.5255324099163289858177390, 0.7966664774136267395915539, 0.9602898564975362316835609])
        w = np.array([0.1012285362903762591525314, 0.2223810344533744705443560, 0.3137066458778872873379622, 0.3626837833783619829651504, 0, 0.3626837833783619829651504, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.1012285362903762591525314])
    elif n == 10:
        x = np.array([ -0.9739065285171717200779640, -0.8650633666889845107320967, -0.6794095682990244062343274, -0.4333953941292471907992659, -0.1488743389816312108848260, 0, 0.1488743389816312108848260, 0.4333953941292471907992659, 0.6794095682990244062343274, 0.8650633666889845107320967, 0.9739065285171717200779640])
        w = np.array([ 0.0666713443086881375935688, 0.1494513491505805931457763, 0.2190863625159820439955349, 0.2692667193099963550912269, 0.2955242247147528701738930, 0, 0.2955242247147528701738930, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.0666713443086881375935688])

    return x, w

def mudanca_variavel(a, b, x, w):
    # nós são linearmente transportados e os pesos multiplicados por um fator de escala m
    # a -> -1 e b -> 1
    novo_x = np.zeros(len(x))
    novo_w = np.zeros(len(x))

    for i in range(len(x)):
        novo_x[i] = (x[i] + (a + b)/(b - a)) * (b - a) / 2
        novo_w[i] = w[i] * (b - a) / 2

    return novo_x, novo_w

#def calcula_funcao(f, x):
#    f_x = 0
#    for i in range(len(f)):
#        f_x += f[i]*(x**i)
#
#    return f_x

#def integralGauss(a, b, f, n):
#    x, w = no_peso(n)
#    novo_x , novo_w = mudanca_variavel(a, b, x, w)
#    
#    res = 0
#    for i in range(n + 1):
#        res += novo_w[i]*calcula_funcao(f, novo_x[i])
#
#    return res

def integralGauss(a, b, f, n):
    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(a, b, x, w)
    
    res = 0
    for i in range(n + 1):
        y = novo_x[i]
        res += novo_w[i]*eval(f)

    return res

#def calculaExemplo1Cubo(n):
#    f = [1]
#    ax = [0]
#    bx = [1]
#    ay = [0]
#    by = [1]
#
#    x, w = no_peso(n)
#    g = np.zeros(len(x))
#    res = 0
#    for i in range(len(x)):
#        novo_x, novo_w = mudanca_variavel(calcula_funcao(ax, x[i]), calcula_funcao(bx, x[i]), x, w)
#        g[i] = integralGauss(calcula_funcao(ay, novo_x[i]), calcula_funcao(by, novo_x[i]), f, n)
#        res += novo_w[i]*g[i]
#
#    return res

def calculaExemplo1Cubo(n):
    ax = "0"
    bx = "1"
    ay = "0"
    by = "1"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "1"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo1Tetraedro(n):
    #f = "1 - x - y"
    ax = "0"
    bx = "1"
    ay = "0"
    by = "1 - xi"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        #f_x = 1 - novo_x[i]
        #novo_f = str(f_x) + " - y"
        f = str(1-novo_x[i])+ " - y"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo2Primeira(n):
    ax = "0"
    bx = "1"
    ay = "0"
    by = "1 - xi**2"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "1"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo2Segunda(n):
    ax = "0"
    bx = "1"
    ay = "0"
    by = "(1 - xi)**(1/2)"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "1"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

#def calcula(n):
#
#    #calcular integral normal
#    f = [1]
#    ax = [0]
#    bx = [1]
#    ay = [0]
#    by = [1, 0, -1]
#
#    x, w = no_peso(n)
#    g = np.zeros(len(x))
#    
#    for i in range(len(x)):
#        novo_x, novo_w = mudanca_variavel(calcula_funcao(ax, x[i]), calcula_funcao(bx, x[i]), x, w)
#        g[i] = integralGauss(calcula_funcao(ay, novo_x[i]), calcula_funcao(by, novo_x[i]), f, n)
#    print("g: ", g)
#
#    res = 0
#    for i in range(n + 1):
#        res += novo_w[i]*g[i]
#
#    return res


def main():
    exemplo = int(input("Qual exemplo deseja calcular?\n"))

    if exemplo == 1:
        print("---------- Exemplo 1 ----------")

        print("Para n = 6: ")
        print("Volume do Cubo = ", calculaExemplo1Cubo(6))
        print("Volume do Tetraedro = ", calculaExemplo1Tetraedro(6))

        print("\nPara n = 8: ")
        print("Volume do Cubo = ", calculaExemplo1Cubo(8))
        print("Volume do Tetraedro = ", calculaExemplo1Tetraedro(8))

        print("\nPara n = 10: ")
        print("Volume do Cubo = ", calculaExemplo1Cubo(10))
        print("Volume do Tetraedro = ", calculaExemplo1Tetraedro(10))
    
    elif exemplo == 2:
        print("---------- Exemplo 2 ----------")

        print("Para n = 6: ")
        print("Pela Primeira Integral = ", calculaExemplo2Primeira(6))
        print("Pela Segunda Integral = ", calculaExemplo2Segunda(6))

        print("\nPara n = 8: ")
        print("Pela Primeira Integral = ", calculaExemplo2Primeira(8))
        print("Pela Segunda Integral = ", calculaExemplo2Segunda(8))

        print("\nPara n = 10: ")
        print("Pela Primeira Integral = ", calculaExemplo2Primeira(10))
        print("Pela Segunda Integral = ", calculaExemplo2Segunda(10))

    elif exemplo == 3:
        print("---------- Exemplo 3 ----------")

    elif exemplo == 4:
        print("---------- Exemplo 4 ----------")

    else:
        print("Não existe o Exemplo", exemplo)

if __name__ == "__main__":
    main()
