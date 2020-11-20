
import numpy as np
import control as ctl
from matplotlib import pyplot as plt

'''
Recebe a Funcao de transferencia e:
- Retorna os polos e zeros;
- Retorna o espaço de estados;
- Plota no tempo a resposta ao impulso unitario;
- Plota no tempo a resposta ao degrau unitario.

########################################################
Input (Funcao de transferencia)
########################################################
'''
num = [1.421e-14, 0.0003226, 0.03458, 1.615]
den = [1,21,976.4,8351, 164400]
# num = [1, 0.01]
# den = [1,9,18,0,0]

G = ctl.tf(num, den)
print('G =', G)


########################################################
#  Espaco de estados
########################################################
S = ctl.tf2ss(G)
print('S:\n', S)


########################################################
#  Polos e zeros
########################################################
(p, z) = ctl.pzmap(G)
print('polos =', p)
print('zeros =', z)
plt.show()


########################################################
#  Plot da resp no dominio do tempo ao impulso unitário
########################################################
# T, yout = ctl.impulse_response(G)
# plt.plot(T, yout)
# plt.show()


########################################################
#  Plot da resp no dominio do tempo ao degrau unitário
########################################################
T, yout = ctl.step_response(G)
plt.plot(T, 1000*yout)
plt.title('Resposta a um degrau', fontsize=16)
ax = plt.axes()
ax.set_xlabel('t [s]', fontsize=14)
ax.set_ylabel('x [mm]', fontsize=14)
plt.grid()
plt.show()


