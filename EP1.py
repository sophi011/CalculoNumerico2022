import numpy as np

def criar_exemplo(n):    
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

def decomposicao_nao_ciclica(a, b, c):
    # decomposicao nos vetores l e u
    n = len(a)
    u = np.zeros(n)
    l = np.zeros(n)

    u[0] = b[0]
    for i in range(1, n):
        l[i] = a[i]/u[i-1]
        u[i] = b[i] - (l[i] * c[i-1])

    return l, u

def res_sist_linear(l, u, c, d):
    # resolucao de sistema linear a partir dos vetores l, u, c, d
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
        x[i] = (y[i] - c[i] * x[i+1])/u[i]

    return x

def resolve_ciclica(a, b, c, d):
    # resolve uma matriz tridiagonal ciclica
    n = len(d)

    # criacao da submatriz T
    a_t = np.copy(a[:n-1])
    a_t[0] = 0
    b_t = np.copy(b[:n-1])
    c_t = np.copy(c[:n-1])
    c_t[-1] = 0
    d_t = np.copy(d[:n-1])
    v = np.zeros(n-1)
    v[0] = a[0]
    v[-1] = c[n-2]

    # decompoe a submatriz T
    l, u = decomposicao_nao_ciclica(a_t, b_t, c_t)
    
    # achar os valores ed y_t e z_t
    y_t = res_sist_linear(l, u, c_t, d_t)
    z_t = res_sist_linear(l, u, c_t, v)

    # calculo de x
    x_n = (d[n-1] - c[n-1]*y_t[0] - a[n-1]*y_t[n-2])/(b[n-1]-c[n-1]*z_t[0]-a[n-1]*z_t[n-2])
    x_t = y_t - x_n*z_t
    x = np.append(x_t, x_n)

    return x

def decompoe_aumentada(MA):
    # decompoe a matriz aumentada do sistema Ax=d em A e d
    n = len(MA)
    d = np.copy(MA[:, n])
    A = np.copy(MA[:, :n])    
    print("d:", d)
    print("A:", A)
    return A, d

def resolve_matriz(A, d):
    # resolve o sistema linear a partir da matriz tridiagonal dada
    n = len(A)
    a, b, c = matriz_to_vetores(A)
    
    # checar se a matriz eh ciclica
    if A[0][n-1] != 0 or A[n-1][0] != 0:
        x = resolve_ciclica(a, b, c, d)
    else:
        l, u = decomposicao_nao_ciclica(a, b, c)
        x = res_sist_linear(l, u, c, d)
    return x
    
def resolve_vetor(a, b, c, d):
    # resolve o sistema linear a partir da matriz tridiagonal aumentada decomposta em a, b, c e d
    n = len(a)

    # checar se a matriz eh ciclica
    if a[0] != 0 or c[n-1] != 0:
        x = resolve_ciclica(a, b, c, d)
    else:
        l, u = decomposicao_nao_ciclica(a, b, c)
        x = res_sist_linear(l, u, c, d)
    return x

def resolve_exemplo(n):
    a, b, c, d = criar_exemplo(n)
    x = resolve_ciclica(a, b, c, d)
    return x


def main():
    n = int(input("Indique a dimensão da matriz de entrada: "))
    op = int(input("Selecione a opcao de entrada:\n 1. Matriz Tridiagonal \n 2. Vetores da Matriz Tridiagonal \n 3. Vetores da Matriz de Exemplo \nOpcao desejada: "))
    
    if op == 1:
        # 1. Matriz Tridiagonal Aumentada
        au = int(input("Deseja inserir:\n 1. Matriz A e o vetor d\n 2. Matriz Aumentada MA\nOpcao desejada: "))
        if au == 1:
            # 1. Matriz A e o vetor d
            A = np.zeros((n,n))
            for i in range(n):
                for j in range(n):
                    A[i,j] = float(input("Valor de A[%d][%d]: " %(i, j)))
            
            d = np.zeros(n)
            for i in range(n):
                d[i] = float(input("Valor de d[%d]: " %(i)))
        
        elif au == 2:
            # 2. Matriz Aumentada MA
            MA = np.zeros((n, n+1))
            for i in range(n):
                for j in range(n+1):
                    MA[i,j] = float(input("Valor de MA[%d][%d]: " %(i, j)))         
            A, d = decompoe_aumentada(MA)
        
        else:
            print("Opcao invalida!")
            return 0

        x = resolve_matriz(A, d)

    elif op == 2:
        # 2. Vetores da Matriz Tridiagonal
        a = np.zeros(n)
        b = np.zeros(n)
        c = np.zeros(n)
        d = np.zeros(n)

        for i in range(n):
            a[i] = float(input("Valor de a[%d]: " %(i)))
        for i in range(n):
            b[i] = float(input("Valor de b[%d]: " %(i)))
        for i in range(n):
            c[i] = float(input("Valor de c[%d]: " %(i)))
        for i in range(n):
            d[i] = float(input("Valor de d[%d]: " %(i)))

        x = resolve_vetor(a, b, c, d)  
        
    elif op == 3:
        # 3. Vetores da Matriz de Exemplo
        x = resolve_exemplo(n)
          
    else:
        print("Opcao invalida!")   
        return 0 

    print("A solução do sistema apresentado é x = ", x)   

if __name__ == "__main__":
    main()
