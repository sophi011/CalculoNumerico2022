"""
Autoria do código
Gabriela Yuri Ishikawa - NºUSP: 11804098
Sophia Celine Rafael Alves Pereira - NºUSP: 11803994
"""
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
    # Muda os limites de integracao para -1 e 1, fazendo as mudancas necessarias na funcao
    # a -> -1 e b -> 1
    novo_x = np.zeros(len(x))
    novo_w = np.zeros(len(x))

    for i in range(len(x)):
        novo_x[i] = (x[i] + (a + b)/(b - a)) * (b - a) / 2
        novo_w[i] = w[i] * (b - a) / 2

    return novo_x, novo_w

def calculaIntegral(ax, bx, ay, by, f, n):
    # Recebe os limites de integracao e retorna a integral calculada pela formula de integracao numerica de Gauss
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

def main():
    exemplo = int(input("Qual exemplo deseja calcular?\n"))

    if exemplo == 1:
        print("---------- Exemplo 1 ----------")
        # Cubo
        ax_cubo = "0"
        bx_cubo = "1"
        ay_cubo = "0"
        by_cubo = "1"
        f_cubo = "1"    
        # Tetraedro: f = "1 - x - y"
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
        # Primeira integral
        ax1 = "0"
        bx1 = "1"
        ay1 = "0"
        by1 = "1 - xi**2"
        f1 = "1"
        # Segunda integral
        ax2 = "0"
        bx2 = "1"
        ay2 = "0"
        by2 = "(1 - xi)**(1/2)"
        f2 = "1"

        print("Para n = 6: ")
        print("Pela Primeira Integral = ", calculaIntegral(ax1, bx1, ay1, by1, f1, 6))
        print("Pela Segunda Integral = ", calculaIntegral(ax2, bx2, ay2, by2, f2, 6))

        print("\nPara n = 8: ")
        print("Pela Primeira Integral = ", calculaIntegral(ax1, bx1, ay1, by1, f1, 8))
        print("Pela Segunda Integral = ", calculaIntegral(ax2, bx2, ay2, by2, f2, 8))

        print("\nPara n = 10: ")
        print("Pela Primeira Integral = ", calculaIntegral(ax1, bx1, ay1, by1, f1, 10))
        print("Pela Segunda Integral = ", calculaIntegral(ax2, bx2, ay2, by2, f2, 10))

    elif exemplo == 3:
        print("---------- Exemplo 3 ----------")
        # Calculo da are
        axArea = "0.1"
        bxArea = "0.5"
        ayArea = "xi**3"
        byArea = "xi**2"
        fArea = "((y**2 *"+ str(np.e) + "**(2*y/xi)) / (xi**4) + (" + str(np.e) + "**(2*y/xi)) / (xi**2) + 1)**(1/2)"
        # Calculo do volume
        axVolume = "0.1"
        bxVolume = "0.5"
        ayVolume = "xi**3"
        byVolume = "xi**2"
        fVolume = str(np.e)+ "**(y/xi)"

        print("Para n = 6: ")
        print("Área da superfície = ", calculaIntegral(axArea, bxArea, ayArea, byArea, fArea, 6))
        print("Volume abaixo da superfície = ", calculaIntegral(axVolume, bxVolume, ayVolume, byVolume, fVolume, 6))


        print("\nPara n = 8: ")
        print("Área da superfície = ", calculaIntegral(axArea, bxArea, ayArea, byArea, fArea, 8))
        print("Volume abaixo da superfície = ", calculaIntegral(axVolume, bxVolume, ayVolume, byVolume, fVolume, 8))

        print("\nPara n = 10: ")
        print("Área da superfície = ", calculaIntegral(axArea, bxArea, ayArea, byArea, fArea, 10))
        print("Volume abaixo da superfície = ", calculaIntegral(axVolume, bxVolume, ayVolume, byVolume, fVolume, 10))

    elif exemplo == 4:
        print("---------- Exemplo 4 ----------")
        # Volume da calota
        axCalota = "3/4"
        bxCalota = "1"
        ayCalota = "0"
        byCalota = "(1 - xi**2)**(1/2)"
        fCalota = str(2*np.pi) + "*y"
        # Volume do solido de revolucao
        axSolido = "-1"
        bxSolido = "1"
        aySolido = "0"
        bySolido = str(np.e) + "**(-xi**2)"
        fSolido = str(2*np.pi) + "*y"

        print("Para n = 6: ")
        print("Volume da Calota = ", calculaIntegral(axCalota, bxCalota, ayCalota, byCalota, fCalota, 6))
        print("Volume do Sólido de Revolução = ", calculaIntegral(axSolido, bxSolido, aySolido, bySolido, fSolido, 6))

        print("\nPara n = 8: ")
        print("Volume da Calota = ", calculaIntegral(axCalota, bxCalota, ayCalota, byCalota, fCalota, 8))
        print("Volume do Sólido de Revolução = ", calculaIntegral(axSolido, bxSolido, aySolido, bySolido, fSolido, 6))

        print("\nPara n = 10: ")
        print("Volume da Calota = ", calculaIntegral(axCalota, bxCalota, ayCalota, byCalota, fCalota, 8))
        print("Volume do Sólido de Revolução = ", calculaIntegral(axSolido, bxSolido, aySolido, bySolido, fSolido, 6))

    else:
        print("Não existe o Exemplo", exemplo)

if __name__ == "__main__":
    main()
