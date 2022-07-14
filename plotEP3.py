import numpy as np
import matplotlib.pyplot as plt
import EP3

def plot_calor_cte():
    Q, comp, temp = EP3.calcula_calor_cte(31)

    temp2 = np.zeros(len(comp))
    temp2[1:-1] = temp
    temp2[0] = 20
    temp2[-1] = 20

    Qvec = [Q]*(len(comp))
    fig, axs = plt.subplots(2, 1)
    fig.suptitle('Comportamento térmico com geração de calor e resfriamento constantes', fontsize=16)
    plt.subplot(2, 1, 1)
    plt.xlabel('x (mm)')
    plt.ylabel('Q(x) (W/m)')
    plt.plot(comp, Qvec)
    plt.subplot(2, 1, 2)
    plt.xlabel('x (mm)')
    plt.ylabel('Temperatura (°C)')
    plt.plot(comp, temp2)
    plt.show()

def plot_gaussianas():
    a = 20
    b = 20
    Q, comp, temp = EP3.calcula_calor_gaussiana(750000, 10000, 0.02, 0.01, 1, 31, a, b)
    temp2 = np.zeros(len(comp))
    Qvec = np.zeros(len(comp))
    temp2[1:-1] = temp
    temp2[0] = a
    temp2[-1] = b
    for i in range(len(comp)):
        x = comp[i]
        Qvec[i] = eval(Q)
    fig, axs = plt.subplots(2, 1)
    fig.suptitle('Comportamento térmico com geração de calor e resfriamento como funções gaussianas', fontsize=16)
    plt.subplot(2, 1, 1)
    plt.xlabel('x (mm)')
    plt.ylabel('Q(x) (W/m)')
    plt.plot(comp, Qvec)
    plt.subplot(2, 1, 2)
    plt.xlabel('x (mm)')
    plt.ylabel('Temperatura (°C)')
    plt.plot(comp, temp2)
    plt.show()

def plot_var_material():

    a = 0
    b = 0
    ks = 3.6
    ka = 60
    n = 31
    L = 0.02
    d = 0.005
    Q, comp, temp = EP3.calcula_var_material(n, ks, ka, L, d, a, b)
    Qvec = np.zeros(len(comp))
    for i in range(len(comp)):
        x = comp[i]
        Qvec[i] = eval(Q)
    fig, axs = plt.subplots(2, 1)
    fig.suptitle('Comportamento térmico com variação de material', fontsize=16)
    plt.subplot(2, 1, 1)
    plt.xlabel('x (mm)')
    plt.ylabel('Q(x) (W/m)')
    plt.plot(comp, Qvec)
    plt.subplot(2, 1, 2)
    plt.xlabel('x (mm)')
    plt.ylabel('Temperatura (°C)')
    plt.plot(comp, temp)
    plt.show()

if __name__ == "__main__":
    #plot_calor_cte()
    #plot_gaussianas()
    plot_var_material()

