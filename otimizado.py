
def calculaIntegral(ax, bx, ay, by, f, n):
    x, w = no_peso(n)
    novo_x, novo_w = mudanca_variavel(eval(ax), eval(bx), x, w)

    g = np.zeros(len(x))
    res = 0

    for i in range(len(x)):
        xi = novo_x[i]
        g[i] = integralGauss(eval(ay), eval(by), f, n)
        res += novo_w[i]*g[i]

    return res

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

        ax_cubo = "0"
        bx_cubo = "1"
        ay_cubo = "0"
        by_cubo = "1"
        f_cubo = "1"    
        #f = "1 - x - y"
        ax_tetra = "0"
        bx_tetra = "1"
        ay_tetra = "0"
        by_tetra = "1 - xi"
        f_tetra = str(1-novo_x[i])+ " - y"
        print("Para n = 6, calculaIntegral cubo = ", calculaIntegral(ax, bx, ay, by, f, 6))

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