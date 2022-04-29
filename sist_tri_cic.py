import numpy as np

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

def decomposicao_nao_ciclica(a, b, c):
    # vetores l e u
    n = len(a)
    u = np.zeros(n)
    l = np.zeros(n)

    u[0] = b[0]
    for i in range(1, n):
        l[i] = a[i]/u[i-1]
        u[i] = b[i] - (l[i] * c[i-1])
    
    print("l: ", l)
    print("u: ", u)
    return l, u

def res_sist_linear_tri(a, b, c, d):

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

def main():
    # entrada n do tamanho da matriz desejada
    n = int(input("Digite o valor de n: "))

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

    print("x_t: ", x_t)
    print("x_n: ", x_n)

    #print("a_t: ", a_t)
    #print("b_t: ", b_t)
    #print("c_t: ", c_t)
    #print("d_t: ", d_t)
    #print("v: ", v)
    #print("w: ", w)

if __name__ == "__main__":
    main()