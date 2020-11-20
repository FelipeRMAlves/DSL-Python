import numpy as np
import control as ctl
from matplotlib import pyplot as plt
from shapely.geometry import LineString, point

'''
Recebe o espaco de estados e
- Retorna os polos e zeros
- Retorna a funcao de transferencia
- Plota no tempo a resposta ao impulso unitario
- Plota no tempo a resposta ao degrau unitario
- Plota o tempo de acomodacao.

#########################################################
Input (espaco de estados)
#########################################################
'''
# System matrices as 2D arrays :
A = np.array([[0, 0, 1, 0], 
              [0, 0, 0, 1], 
              [-490, -137, -12, -2], 
              [-170, -383, -2.3, -9]])
B = np.array([[0], 
              [0], 
              [1000/310], 
              [-693/250]])
C = np.array([[1, 0, 0, 0]])
# C = np.array([[0, 1, 0, 0]])
D = np.array([[0]])

S = ctl.ss(A, B, C, D)
print('S =', S)


#########################################################
#  Funcao de transferencia
#########################################################
G = ctl.ss2tf(S)
print('G =', G)


#########################################################
#  Polos e zeros
#########################################################
(p, z) = ctl.pzmap(G)
print('polos =', p)
print('zeros =', z)
plt.show()


#########################################################
#  Plot da resp no dominio do tempo ao impulso unitario
#########################################################
# T, yout = ctl.impulse_response(G)
# plt.plot(T, yout)
# plt.show()


#########################################################
#  Plot da resp no dominio do tempo ao degrau unitario
#########################################################
T, yout = ctl.step_response(G)
plt.plot(T, yout)
# plt.plot(T, 180*yout/np.pi)
# plt.title('Resposta a um degrau', fontsize=16)
ax = plt.axes()
ax.set_xlabel('t [s]', fontsize=14)
ax.set_ylabel('x [m]', fontsize=14)
# ax.set_ylabel('[graus]', fontsize=14)
plt.grid()


#########################################################
#  Funcao que acha o valor mais proximo de Ts
#########################################################
def find_nearest(array, value):
    #  funcao para descobrir valor mais proximo na lista
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


#########################################################
#  Funcao que acha e plota intersecao do Tp com a respost
#########################################################
def intersecao(x1, y1, x2, y2):
    # x1 = lista eixo x curva 1
    # y1 = lista eixo y curva 1
    # x2 = lista eixo x curva 2
    # y2 = lista eixo y curva 2

    first_line = LineString(np.column_stack((x1, y1)))
    second_line = LineString(np.column_stack((x2, y2)))
    intersection = first_line.intersection(second_line)

    global x
    global y
    if intersection.geom_type == 'MultiPoint':
        plt.plot(*LineString(intersection).xy, 'go')
        try:
            x, y = LineString(intersection).xy
            print(' x1= ', x[-1], '\n', 'y1= ', y[-1])
        except:
            pass

    elif intersection.geom_type == 'Point':
        plt.plot(*intersection.xy, 'go')
        try:
            x, y = intersection.xy
            print(' x= ', x[-1], '\n', 'y= ', y[-1])

        except:
            pass


#########################################################
#  Plot final de Ts (tempo de acomodacao)
#########################################################
valor_final = yout[-1]
print(valor_final)
minTp = 0.98 * valor_final * np.ones(len(T))
maxTp = 1.02 * valor_final * np.ones(len(T))
intersecao(T,yout,T, minTp)
intersecao(T,yout,T, maxTp)
plt.plot(T, minTp, 'r-')
plt.plot(T, maxTp, 'r-')
plt.title('Tempo de acomodacao', fontsize=16)


plt.show()