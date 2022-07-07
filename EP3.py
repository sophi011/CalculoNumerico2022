

import numpy as np
import EP1
import EP2

def monta_splines(n, f):
    h = 1/(n+1) # tamanho de cada intervalo dentro de [0, 1]
    x = [0]*(n+2)
    print(x)
    phi1 = [0]*(n+2)
    phi2 = [0]*(n+2)
    
    print(len(x))
    for i in range(n+2):  # define os valores dos nós
        x[i] = i*h

    for i in range(1, n+1):
        xi_ant = str(x[i-1])
        xi_pos = str(x[i+1])

        phi1[i] = "(x - " + xi_ant + ")/" + str(h)  # vale de xi-1 até xi
        phi2[i] = "(" + xi_pos + " - x)/" + str(h)  # vale de xi até xi+1
        
    
    print(phi1)
    print(phi2)




def main():
    pass

monta_splines(6, 1)