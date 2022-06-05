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

def calcula_funcao(f, x):
    f_x = 0
    for i in range(len(f)):
        f_x += f[i]*x**i
    
    return f_x

def mudanca_variavel(a, b, x, w):
    # nós são linearmente transportados e os pesos multiplicados por um fator de escala m
    # a -> -1 e b -> 1
    novo_x = np.zeros(len(x))
    novo_w = np.zeros(len(x))
    #m = (b-a)/2
    for i in range(len(x)):
        a_x = calcula_funcao(a, x[i])
        b_x = calcula_funcao(b, x[i])
        #a_x = a
        #b_x = b
        #novo_x[i] = (2 * x[i] - (a_x + b_x)) / (b_x - a_x)
        novo_x[i] = (x[i] + (a_x+b_x)/(b_x-a_x)) * (b_x-a_x)/2
        novo_w[i] = w[i] * (b_x - a_x) / 2

    return novo_x, novo_w

def integralGauss(x, w, f):
    res = 0

    for i in range(len(x)):
        f_x = calcula_funcao(f, x[i])
        res += w[i]*f_x

    return res

def exemplo1cubo(n):
    f = [1]
    a1= [0]
    b1 = [1]
    a2= [0]
    b2 = [1, -1]

    x, w = no_peso(n)
    x_1, w_1 = mudanca_variavel(a1, b1, x, w) #x e w da integral de fora
    
    novo_a2 = np.zeros(len(x))
    novo_b2 = np.zeros(len(x))

    for i in range(n+1):
        novo_a2[i] = calcula_funcao(a2, x_1[i])
        novo_b2[i] = calcula_funcao(b2, x_1[i])
    res = 0
    for i in range(n+1):
        x_2, w_2 = mudanca_variavel([novo_a2[i]], [novo_b2[i]], x, w)
        #res = integralGauss(x_1, w_1, [integralGauss(x_2, w_2, f)])
        res += w_1[i]*integralGauss(x_2, w_2, f)
    
    print("Resposta: ", res)
    return x_1, w_1

def main():
    print("Para n = 6:")
    x, w = exemplo1cubo(6)
    #print("x: ", x)
    #print("w: ", w)

    print("Para n = 8:")
    x, w = exemplo1cubo(8)
    #print("x: ", x)
    #print("w: ", w)

    
    print("Para n = 10:")
    x, w = exemplo1cubo(10)
    #print("x: ", x)
    #print("w: ", w)

    #x, w = mudanca_variavel(0, 1, 6)
    #print("x: ", x)
    #print("w: ", w)

if __name__ == "__main__":
    main()