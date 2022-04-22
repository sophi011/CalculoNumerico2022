import numpy as np
import sys
import time


# DECOMPOSICAO LU
# matriz A
#n = 3
#a = np.zeros(n)
#b = np.zeros(n)
#c = np.zeros(n)

#| 2 1 0 0 |
#| 2 2 1 0 |
#| 0 3 2 1 |
#| 0 0 3 2 |

a = np.array([0, 2.0, 3.0, 3.0])
b = np.array([2.0, 2.0, 2.0, 2.0])
c = np.array([1.0, 1.0, 1.0, 0])
n = len(b)

# vetores l e u
u = np.zeros(n)
l = np.zeros(n)

u[0] = b[0]
for i in range(1, n):
    l[i] = a[i]/u[i-1]
    u[i] = b[i] - (l[i] * c[i-1])

# criando as matrizes L e U
U = np.zeros((n, n))
L = np.zeros((n, n))
for i in range(n-1):
    U[i, i+1] = c[i]
    L[i+1, i] = l[i+1]

# diagonais de L e de U
np.fill_diagonal(L, 1)
for i in range(n):
    U[i, i] = u[i]

# conferindo o resultado
A = np.dot(L,U)
print("A: \n", A)


# RESOLUCAO DO SISTEMA LINEAR
#L y = d
d = np.zeros(n)
d = np.array([1, 1, 1, 1])

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
y[0] = d[0]
for i in range(1,n,1):
    #Vetorizei aqui!
    y[i] = (d[i] - np.dot(LU[i,:i], y[:i]))

# Ux=y
x = np.zeros(n)
x[n-1] = y[n-1]/LU[n-1,n-1]
for i in range(n-2,-1,-1):
    #Vetorizei aqui!
    x[i] = (y[i] - np.dot(LU[i,i+1:], x[i+1:]))/LU[i,i]


print("y: \n", y)
print("x:\n", x)