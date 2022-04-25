import numpy as np
import sys
import time

def elim_gauss(A, b, n):

#    a = create_matrix(n)
#    
#    A = np.copy(a[:,:-1])
#    b = np.copy(a[:,n]).reshape((n))
    
    start_time = time.time()
    
    #Guardo tanto L quanto U em uma unica matriz!!!!
    LU = np.eye(n)
    # @ faz multiplicacao de matrizes usando numpy
    for i in range(n):
        #Varre linhas superiores (Upper)
        LU[i,i:] = A[i,i:]-LU[i,:i] @ LU[:i,i:]
        #Varre colunas inferiores (Lower)
        LU[(i+1):,i] = ( A[(i+1):,i]- LU[(i+1):,:i] @ LU[:i,i] ) / LU[i,i]
    
    
    # Substituicao
    # LUx=b
    # Ly=b
    y = np.zeros(n)
    # Ly=b
    y[0] = b[0]
    for i in range(1,n,1):
        #Vetorizei aqui!
        y[i] = (b[i] - np.dot(LU[i,:i], y[:i]))
    
    # Ux=y
    x = np.zeros(n)
    x[n-1] = y[n-1]/LU[n-1,n-1]
    for i in range(n-2,-1,-1):
        #Vetorizei aqui!
        x[i] = (y[i] - np.dot(LU[i,i+1:], x[i+1:]))/LU[i,i]
    
    tempo = time.time() - start_time
    
    print("Soma da Solucao:", np.sum(x), " Tempo que levou: ", tempo)
    
    # Solucao
    print('\nSolucao: ')
    print(x[0])
    print('\nTeste: ')
    print(np.max(np.abs(A@x- b)))
    
    #Testes
    U = np.triu(LU)
    L = np.tril(LU)
    np.fill_diagonal(L, 1.0)
    print('\nTeste LU: ')
    print(np.max(np.max(np.abs(L@U-A))))

    return x, y