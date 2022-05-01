import numpy as np
import math
import sys
import time

def criar_matriz(n):
    
    # criacao da matriz com as equacoes dadas no enunciado
    a = np.zeros(n)
    b = np.full((n),2)
    d = np.zeros(n)

    for i in range(n-1):
        a[i] = (2*(i+1) - 1)/(4*(i+1))
        d[i] = np.cos((2*np.pi*(i+1)**2)/n**2)

    a[n-1] = (2*n - 1)/(2*n)
    d[n-1] = np.cos((2*np.pi*n**2)/n**2)
    c = 1 - a

    return a, b, c, d

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
    for i in range(n):
        A[i,i] = b[i]
        A[i,i-1] = a[i]
        if i+1 == n:
            A[i,0] = c[i]
        else:
            A[i,i+1] = c[i]

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

    return l, u

# RESOLUCAO DO SISTEMA LINEAR
# A x = b
# L y = d
# U x = y

def res_sist_linear_tri(a, b, c, d):
    # resolucao de sistema linear com matriz tridiagonal nao ciclica

    l, u = decomposicao_nao_ciclica(a, b, c)
    n = len(d)
    y = np.zeros(n)

    #L y = d:
    y[0] = d[0]
    for i in range(1, n):
        y[i] = d[i] - (l[i] * y[i-1])

    #U x = y:
    x = np.zeros(n)

    x[n-1] = y[n-1]/u[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - c[i]*x[i+1])/u[i]

    #print("x:\n", x)
    return x

def res_sist_cic(n):

    # criar a matriz a partir do n dado
    a, b, c, d = criar_matriz(n)

    #print("a: ", a)
    #print("b: ", b)
    #print("c: ", c)
    #print("d: ", d)

    a_t = np.copy(a[:n-1])
    a_t[0] = 0
    b_t = np.copy(b[:n-1])
    c_t = np.copy(c[:n-1])
    c_t[-1] = 0
    d_t = np.copy(d[:n-1])
    v = np.zeros(n-1)
    v[0] = a[0]
    v[-1] = c[n-2]
    w = np.zeros(n-1)
    w[0] = c[n-1]
    w[-1] = a[n-1]

    # para achar o y_t
    y_t = res_sist_linear_tri(a_t, b_t, c_t, d_t)
    print("y_t: ", y_t)

    z_t = res_sist_linear_tri(a_t, b_t, c_t, v)
    print("z_t: ", z_t)

    x_n = (d[n-1] - c[n-1]*y_t[0] - a[n-1]*y_t[n-2])/(b[n-1]-c[n-1]*z_t[0]-a[n-1]*z_t[n-2])

    x_t = y_t - x_n*z_t

    x = np.append(x_t, x_n)

    return x

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
        A = vetores_to_matriz(a, b, c)
        print("A: ", A)
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
    

if __name__ == "__main__":
    main()
