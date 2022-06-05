import math
import numpy as np

def no_peso(n):
    # x[j] = -x[j] <-> w[j]
    if n == 6:
        x = np.array([-0.9324695142031520278123016, -0.6612093864662645136613996, -0.2386191860831969086305017, 
        0, 0.2386191860831969086305017, 0.6612093864662645136613996, 0.9324695142031520278123016])
        w = np.array([0.1713244923791703450402961 , 0.3607615730481386075698335, 0.4679139345726910473898703, 
        0, 0.4679139345726910473898703, 0.3607615730481386075698335, 0.1713244923791703450402961])
    elif n == 8:
        x = np.array([-0.9602898564975362316835609, -0.7966664774136267395915539, -0.5255324099163289858177390, -0.1834346424956498049394761, 
        0, 0.1834346424956498049394761, 0.5255324099163289858177390, 0.7966664774136267395915539, 0.9602898564975362316835609])
        w = np.array([0.1012285362903762591525314, 0.2223810344533744705443560, 0.3137066458778872873379622, 0.3626837833783619829651504, 
        0, 0.3626837833783619829651504, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.1012285362903762591525314])
    elif n == 10:
        x = np.array([ -0.9739065285171717200779640, -0.8650633666889845107320967, -0.6794095682990244062343274, -0.4333953941292471907992659, -0.1488743389816312108848260, 
        0, 0.1488743389816312108848260, 0.4333953941292471907992659, 0.6794095682990244062343274, 0.8650633666889845107320967, 0.9739065285171717200779640])
        w = np.array([ 0.0666713443086881375935688, 0.1494513491505805931457763, 0.2190863625159820439955349, 0.2692667193099963550912269, 0.2955242247147528701738930, 
        0, 0.2955242247147528701738930, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.0666713443086881375935688])

    return x, w

def mudanca_variavel(a, b, x, w):
    # a -> -1 e b -> 1
    novo_x = np.zeros(len(x))
    novo_w = np.zeros(len(x))

    for i in range(len(x)):
        novo_x[i] = (x[i] + (a + b)/(b - a)) * (b - a) / 2
        novo_w[i] = w[i] * (b - a) / 2

    return novo_x, novo_w

def integralGauss(a, b, f, n):
    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(a, b, x, w)
    
    res = 0
    for i in range(n + 1):
        y = novo_x[i]
        res += novo_w[i]*eval(f) # f em funcao de y

    return res

def calculaIntegral(ax, bx, ay, by, f, n):
    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]

        novo_x_y, novo_w_y = mudanca_variavel(eval(ay), eval(by), x, w)
        g[i] = 0
        for j in range(n + 1):
            y = novo_x_y[j]
            g[i] += novo_w_y[j]*eval(f)

        res += novo_w[i]*g[i]

    return res

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

def calculaExemplo3Area(n):
    ax = "0.1"
    bx = "0.5"
    ay = "xi**3"
    by = "xi**2"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "((y**2 *"+ str(np.e) + "**(2*y/" + str(novo_x[i]) +  ")) / (" + str(novo_x[i]) +  "**4) + (" + str(np.e) + "**(2*y/" + str(novo_x[i]) +  ")) / (" + str(novo_x[i]) +  "**2) + 1)**(1/2)"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo3Volume(n):
    ax = "0.1"
    bx = "0.5"
    ay = "xi**3"
    by = "xi**2"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = str(np.e)+ "**(y/" + str(novo_x[i]) + ")"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo4Solido(n):
    ax = "3/4"
    bx = "1"
    ay = "0"
    by = "(1 - xi**2)**(1/2)"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "y"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    res = 2*np.pi*res
    return res

def main():
    exemplo = int(input("Qual exemplo deseja calcular?\n"))

    if exemplo == 1:
        print("---------- Exemplo 1 ----------")

        ax_cubo = "0"
        bx_cubo = "1"
        ay_cubo = "0"
        by_cubo = "1"
        f_cubo = "1"    
        #Tetraedro: f = "1 - x - y"
        ax_tetra = "0"
        bx_tetra = "1"
        ay_tetra = "0"
        by_tetra = "1 - xi"
        f_tetra = "1 - xi - y"

        print("Para n = 6: ")
        print("Volume do Cubo = ", calculaIntegral(ax_cubo, bx_cubo, ay_cubo, by_cubo, f_cubo, 6))
        print("Volume do Tetraedro = ", calculaIntegral(ax_tetra, bx_tetra, ay_tetra, by_tetra, f_tetra, 6))

        print("\nPara n = 8: ")
        print("Volume do Cubo = ", calculaIntegral(ax_cubo, bx_cubo, ay_cubo, by_cubo, f_cubo, 8))
        print("Volume do Tetraedro = ", calculaIntegral(ax_tetra, bx_tetra, ay_tetra, by_tetra, f_tetra, 8))

        print("\nPara n = 10: ")
        print("Volume do Cubo = ", calculaIntegral(ax_cubo, bx_cubo, ay_cubo, by_cubo, f_cubo, 10))
        print("Volume do Tetraedro = ", calculaIntegral(ax_tetra, bx_tetra, ay_tetra, by_tetra, f_tetra, 10))

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

        print("Para n = 6: ")
        print("Área = ", calculaExemplo3Area(6))
        print("Volume = ", calculaExemplo3Volume(6))

        print("Para n = 8: ")
        print("Área = ", calculaExemplo3Area(8))
        print("Volume = ", calculaExemplo3Volume(8))

        print("Para n = 10: ")
        print("Área = ", calculaExemplo3Area(10))
        print("Volume = ", calculaExemplo3Volume(10))

    elif exemplo == 4:
        print("---------- Exemplo 4 ----------")

    else:
        print("Não existe o Exemplo", exemplo)

if __name__ == "__main__":
    main()

##############################################   FUNÇÕES NAO USADAS   #######################################

def calcula(n):

    #calcular integral normal
    f = [1]
    ax = [0]
    bx = [1]
    ay = [0]
    by = [1, 0, -1]

    x, w = no_peso(n)
    g = np.zeros(len(x))
    
    for i in range(len(x)):
        novo_x, novo_w = mudanca_variavel(calcula_funcao(ax, x[i]), calcula_funcao(bx, x[i]), x, w)
        g[i] = integralGauss(calcula_funcao(ay, novo_x[i]), calcula_funcao(by, novo_x[i]), f, n)
    print("g: ", g)

    res = 0
    for i in range(n + 1):
        res += novo_w[i]*g[i]

    return res

def calcula_funcao(f, x):
    f_x = 0
    for i in range(len(f)):
        f_x += f[i]*(x**i)

    return f_x

def integralGauss(a, b, f, n):
    x, w = no_peso(n)
    novo_x , novo_w = mudanca_variavel(a, b, x, w)
    
    res = 0
    for i in range(n + 1):
        res += novo_w[i]*calcula_funcao(f, novo_x[i])

    return res

def integralGauss(a, b, f, n):
    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(a, b, x, w)
    
    res = 0
    for i in range(n + 1):
        y = novo_x[i]
        res += novo_w[i]*eval(f) # f em funcao de y

    return res

def calculaExemplo1Cubo(n):
    f = [1]
    ax = [0]
    bx = [1]
    ay = [0]
    by = [1]

    x, w = no_peso(n)
    g = np.zeros(len(x))
    res = 0
    for i in range(len(x)):
        novo_x, novo_w = mudanca_variavel(calcula_funcao(ax, x[i]), calcula_funcao(bx, x[i]), x, w)
        g[i] = integralGauss(calcula_funcao(ay, novo_x[i]), calcula_funcao(by, novo_x[i]), f, n)
        res += novo_w[i]*g[i]

    return res

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

def calculaExemplo3Area(n):
    ax = "0.1"
    bx = "0.5"
    ay = "xi**3"
    by = "xi**2"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "((y**2 *"+ str(np.e) + "**(2*y/" + str(novo_x[i]) +  ")) / (" + str(novo_x[i]) +  "**4) + (" + str(np.e) + "**(2*y/" + str(novo_x[i]) +  ")) / (" + str(novo_x[i]) +  "**2) + 1)**(1/2)"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo3Volume(n):
    ax = "0.1"
    bx = "0.5"
    ay = "xi**3"
    by = "xi**2"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = str(np.e)+ "**(y/" + str(novo_x[i]) + ")"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

def calculaExemplo4Calota(n):
    ax = "3/4"
    bx = "1"
    ay = "0"
    by = "(1 - xi**2)**(1/2)"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "y"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    res = 2*np.pi*res
    return res

def calculaExemplo4Solido(n):
    ax = "-1"
    bx = "1"
    ay = "0"
    by = str(np.e) + "**(-xi**2)"

    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        f = "y"
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    res = 2*np.pi*res
    return res