import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import LineString, point
import control.matlab as ctl

'''
Recebe a UP, o S ou o teta desejado
- Retorna os polos e plota eles;
- Traça a LGR e traça:
                      A intersecao com o ponto S
                      ou
                      A instersecao com o eixo imaginario
'''
ramo = 1  # chute o ramo de interesse do LGR (para traçar a intersecao)

'''

################################################################################
Input (Funcao de transferencia)
################################################################################
'''
num = [1.421e-14, 0.0003226, 0.03458, 1.615]
den = [1,21,976.4,8351, 164400]
# num = [1, 0.01]
# den = [1,9,18,0,0]

G = ctl.tf(num, den)
print('G =', G)

'''
################################################################################
#  Input - UP
################################################################################
'''
UP = 20  # %
global eps
eps = -(np.log(UP/100))/(np.sqrt((np.pi**2) + (np.log(UP/100)**2)))  # cos(teta)
teta = np.arccos(eps)
print('ksi = ', eps)

'''
################################################################################
#  Input - teta
################################################################################
'''
# teta = 0.0 # np.arccos([eps])
# eps = np.cos(teta)

'''
################################################################################
#  Input - S (ex: s=-2.5 + 2j) para verificar se cruza a LGR
################################################################################
'''
# x_s = -2.5   # real
# y_s = 2   # complexo
# teta = np.arctan(np.abs(y_s)/np.abs(x_s))
# eps = np.cos(teta)


################################################################################
#  polos e zeros plotados
################################################################################
(p, z) = ctl.pzmap(G)
print('polos =', p)
print('zeros =', z)


################################################################################
#  Lugar geometrico das raizes (LGR)
################################################################################
rlist, klist = ctl.rlocus(G)       # rlist - lugar geometrico das raizes
                                   # klist - ganhos correspondentes

# plotar linha baseada no LGR para achar interseção
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
#  Instersecao com Reta de inclinação referente a eps
################################################################################
minRng = 10
s_real = np.arange(-minRng, 0.0, minRng/len(rlist))
M = np.absolute(s_real / eps)                        # M * cos(teta) = s_real
s_im = M * np.sin(teta)                              # coordenada y (imaginaria)
plt.plot(s_real, s_im, 'm-')

try:
    inter = intersecao(s_real, s_im, real, im)
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '[{} + {}j]'.format(round(i_x,1), round(i_y,1)))
except:
    pass

plt.show()


################################################################################
#  Instersecao com o eixo imaginario
################################################################################
# #Calcule o valor de s para eps wn = 0 (limite estabilidade BIBO)
# max_range = 0.1
# s_real2 = np.zeros(len(rlist))
# s_im2 = np.arange(0, max_range, max_range/len(rlist))
# plt.plot(s_real2, s_im2, 'g-')

# try:
#     inter2 = intersecao(s_real2, s_im2, real, im)
#     for i_x, i_y in zip(x, y):
#         plt.text(i_x, i_y, '[{} + {}j]'.format(round(i_x,1), round(i_y,1)))
# except:
#     pass

# plt.show()
