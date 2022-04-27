import numpy as np
import math
import sys
import time

def matriz_to_vetores(A):
    #transforma a matriz tridiagonal de entrada nos vetores a, b, c
    n = len(A)
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    for i in range(n):
        b[i] = A[i,i]
        a[i] = A[i,i-1]
        if i+1 == n:
            c[i] = A[i,0]
        else:
            c[i] = A[i,i+1]
    return a, b, c

def vetores_to_matriz(a, b, c):
    n = len(a)
    A = np.zeros((n, n))
    return A


def decomposicao_nao_ciclica(a, b, c):
    # vetores l e u
    n = len(a)
    u = np.zeros(n)
    l = np.zeros(n)

    u[0] = b[0]
    for i in range(1, n):
        l[i] = a[i]/u[i-1]
        u[i] = b[i] - (l[i] * c[i-1])

    ## criando as matrizes L e U
    #U = np.zeros((n, n))
    #L = np.zeros((n, n))
    #for i in range(n-1):
    #    U[i, i+1] = c[i]
    #    L[i+1, i] = l[i+1]

    ## diagonais de L e de U
    #np.fill_diagonal(L, 1)
    #for i in range(n):
    #    U[i, i] = u[i]

    ## conferindo o resultado
    #A = np.dot(L,U)
    #print("A: \n", A)

    return l, u
    
def decomposicao_ciclica(a, b, c):
    #AAaaAAAAaAAaaa
    pass

def decomposicao_lu(a, b, c):
    #decomposicao da matriz tridiagonal formada pelos vetores a, b e c
    n = len(b)
    
    # se a matriz for ciclica
    if a[0] == 0 or c[n-1] == 0:
        #l, u = decomposicao_nao_ciclica(a, b, c)
        print("decomposicao nao ciclica")
    else:
        #decomposicao_ciclica(a, b, c)
        print("decomposicao ciclica")

# RESOLUCAO DO SISTEMA LINEAR
# A x = b
# L y = d
# U x = y

def res_sist_linear(l, u, c, d):

    n = len(d)
    y = np.zeros(n)
    y[0] = d[0]
    for i in range(1, n):
        y[i] = d[i] - (l[i] * y[i-1])

    print("y: \n", y)

    #U x = y
    x = np.zeros(n)

    x[n-1] = y[n-1]/u[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - c[i]*x[i+1])/u[i]

    print("x:\n", x)
    print("FIM DA NOSSA RESOLUCAO \n\n\n")

    return x, y

#| 2 1 0 0 |
#| 2 2 1 0 |
#| 0 3 2 1 |
#| 0 0 3 2 |


#e1 - matriz
#e2 - vetores a, b, c, d
#e3 - n

#d = np.zeros(n)
#d = np.array([1, 1, 1, 1])
def main():
    op = int(input("Selecione a opcao de entrada:\n 1. Matriz Tridiagonal \n 2. Vetores da Matriz Tridiagonal \n 3. Valor de n \n"))
    if op == 1:
        matriz = np.array([[2, 1, 0, 0], [2, 2, 1, 0], [0, 3, 2, 1], [0, 0, 3, 2]])
        print("matriz\n", matriz)
        d = [1, 1, 1, 1]
        a, b, c = matriz_to_vetores(matriz)

    elif op == 2:
        a = np.array([0, 2.0, 3.0, 3.0])
        b = np.array([2.0, 2.0, 2.0, 2.0])
        c = np.array([1.0, 1.0, 1.0, 0])
        d = [1, 1, 1]

    elif op == 3:
        n = int(input("Digite o valor de n: "))
        a = np.zeros(n)
        b = np.full((n),2)
        d = np.zeros(n)

        for i in range(n-1):
            a[i] = (2*(i+1) - 1)/(4*(i+1))
            d[i] = math.cos((2*math.pi*(i+1)**2)/n**2)

        a[n-1] = (2*n - 1)/(2*n)
        d[n-1] = math.cos((2*math.pi*n**2)/n**2)
        c = 1 - a
    else:
        print("Opcao invalida!")    

    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("d: ", d)
    decomposicao_lu(a, b, c)

if __name__ == "__main__":
    main()
