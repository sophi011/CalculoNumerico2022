"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""

from typing import ItemsView
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

    print("x: ", x)
    print("w: ", w)
    return x, w

def calcular_f(x):
    f = [1, -1]
    f_x = 0
    for i in range(len(f)):
        f_x += f[i]*x**i

    print("f_x: ", f_x)

    return f_x

def mudanca_variavel(a, b, x):
    # nós são linearmente transportados e os pesos multiplicados por um fator de escala m
    # a -> -1 e b -> 1
    novo_x = np.zeros(len(x))
    m = (b-a)/2
    for i in range(len(x)):
        #novo_x[i] = (x[i] + (a+b)/(b-a)) * (b-a)/2
        novo_x[i] = (2*x[i] - (a+b))/(b-a)

    print("novo_x: ", novo_x)
    print("m: ", m)

    return novo_x, m

def integral_gauss(a, b, n):
    # I = w*f(x)
    x, w = no_peso(n)
    res = 0
    if a != -1 or b != 1:
        x, m = mudanca_variavel(a, b, x)
    else:
        m = 1
    for i in range(len(x)):
        f_x = calcular_f(x[i])
        res += w[i]*f_x*m

    return res

def integral_dupla(a1, b1, a2, b2, f, n):
    # usa integral anterior para calcular g
    g = integral_gauss(a2, b2, f, n)
    res = (a2, b2, g, n)

    return res

def main():
    n = int(input("Insira o valor de n: "))
    res = integral_gauss(0, 1, n)
    print("res: ", res)
    # imprimir o valor de n e os valores calculados para cada integral


if __name__ == "__main__":
    main()
