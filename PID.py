
import numpy as np
import sympy as sym
import control.matlab as ctl
import control as cnt
from matplotlib import pyplot as plt
from shapely.geometry import LineString, point

'''
Recebe o Espaço de Estados do sistema e do GPID:
- Retorna a Funcao de transferencia com malha fechada e o PID;
- Plota a LGR com o resultado e a intersecao com a reta de ksi

################################################################################
Input (espaço de estados)
################################################################################
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

Sp = ctl.ss(A, B, C, D)
print('S =', Sp)


################################################################################
#  Funcao de transferencia
################################################################################
G = ctl.ss2tf(Sp)
print('G =', G)

'''
################################################################################
Input (Funcao de transferencia Gpid)
################################################################################
'''
num = np.array([1, 15000.1, 1500])
den = np.array([0, 1, 0])
Gpid = ctl.tf(num, den)
print('Gpid:', Gpid)


################################################################################
#  Em serie (G*Gpid)
################################################################################
S = ctl.series(G, Gpid)


################################################################################
#  Com feedback
################################################################################
F = ctl.feedback(S, 1, -1)
print('Resultado malha fechada:', F)


################################################################################
#  Polos e zeros
################################################################################
# (p, z) = ctl.pzmap(G)
# print('polos =', p)
# print('zeros =', z)
# plt.show()


################################################################################
#  Plot da resp no dominio do tempo ao degrau unitário
################################################################################
T, yout = cnt.step_response(G)
plt.plot(T, 1000*yout)
plt.title('Resposta a um degrau', fontsize=16)
ax = plt.axes()
ax.set_xlabel('t [s]', fontsize=14)
ax.set_ylabel('x [mm]', fontsize=14)
plt.grid()
plt.show()


'''
################################################################################
#  Input - UP
################################################################################
'''
UP = 25  # %
global ksi
ksi = -(np.log(UP/100))/(np.sqrt((np.pi**2) + (np.log(UP/100)**2)))  # cos(teta)
teta = np.arccos(ksi)
print('ksi = ', ksi)


################################################################################
#  Lugar geometrico das raizes (LGR)
################################################################################
rlist, klist = ctl.rlocus(F)       # rlist - lugar geometrico das raizes
                                   # klist - ganhos correspondentes

# plotar linha baseada no LGR para achar interseção
ramo = 3  # chute o ramo de interesse do LGR (para traçar a intersecao)

real = []
im = []
try:
    for j in range(len(rlist)):
        real.append(rlist[j][ramo].real)
        im.append(rlist[j][ramo].imag)
    plt.plot(real, im, 'b-')
except:
    pass


################################################################################
#  Funcao que acha e plota intersecao no LGR
################################################################################
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
        plt.plot(*LineString(intersection).xy, 'mo')
        try:
            x, y = LineString(intersection).xy
            wn1 = y[0]/(np.sqrt(1-(eps**2)))
            wn2 = y[1]/(np.sqrt(1-(eps**2)))
            print(' x1= ', x[0], '\n', 'y1= ', y[0])
            print(' wd1=', y[0], '\n', 'wn1= ', wn1)
            print(' x2= ', x[1], '\n', 'y2= ', y[1])
            print(' wd2=', y[1], '\n', 'wn2= ', wn2)
        except:
            pass

    elif intersection.geom_type == 'Point':
        plt.plot(*intersection.xy, 'mo')
        try:
            x, y = intersection.xy
            wn = y[0]/(np.sqrt(1-(eps**2)))
            print(' x= ', x[0], '\n', 'y= ', y[0])
            print(' wd=', y[0], '\n', 'wn= ', wn)
            print(' Tp=', np.pi/y[0])
            print(' Ts=', 4/(eps*wn))
        except:
            pass


################################################################################
#  Instersecao com Reta de inclinação referente a ksi
################################################################################
minRng = 100
s_real = np.arange(-minRng, 0.0, minRng/len(rlist))
M = np.absolute(s_real / ksi)                        # M * cos(teta) = s_real
s_im = M * np.sin(teta)                              # coordenada y (imaginaria)
plt.plot(s_real, s_im, 'm-')

try:
    inter = intersecao(s_real, s_im, real, im)
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '[{} + {}j]'.format(round(i_x,1), round(i_y,1)))
except:
    pass

plt.show()
