import numpy as np
import control.matlab as ctl
from scipy.signal import tf2ss
from numpy.linalg import matrix_rank

'''
- Calcula os polos atraves do espaco de estados
- Calcula K pela formula de Ackerman;
- Calcula K pelo passo a passo;
- Calcula a matriz de observabilidade;
- Calcula a matriz de controlabilidade.


########################################################
Input (Espaço de estados)
########################################################
'''
A = np.array([[-1, -2],
              [-3, -6]])
B = np.array([[1],
              [0]])
C = np.array([0, 1])
D = np.array([[0]])

# Espaço de estados -> Funcao de transferencia
S = ctl.ss(A, B, C, D)
G = ctl.ss2tf(S)

# Polos a partir do espaço de estados
print('Polos = ', ctl.pole(S))


'''
########################################################
Input (Funcao de transferencia)
########################################################
'''
# num = [0, 0, 1, 0]
# den = [1, 6, 5, 1]
# G = ctl.tf(num, den)

# # Funcao de transferencia -> Espaço de estados
# A, B, C, D = tf2ss(num, den)


print('G(s) =', G)
'''
########################################################
# Input - Polos desejados:
########################################################
'''
poles = [-2+4j, -2-4j]


########################################################
# K - Calculado por Ackerman
########################################################
# Apenas 1 entrada:
K = ctl.acker(A, B, poles)
print('K(ackerman)=', K)

# # Mais de 1 entrada:
# K = ctl.place(A, B, poles)


########################################################
# K - Calculado pelo passo a passo (input alfas)
########################################################
alfa1 = 14
alfa2 = 60

A2 = np.matmul(A, A)     # Matriz A^2
print('A2: \n', A2)

# fi_A:
fi_A = A2 + alfa1*A + alfa2*np.identity(2)
print('fi(A): \n', fi_A)


########################################################
# Matriz de controlabilidade (C)
########################################################
Ct = ctl.ctrb(A, B)
Ct_inv = np.linalg.inv(Ct)
print('Controlabilidade: \n', Ct)
print('Controlabilidade^-1: \n', Ct_inv)
print('det controlab =', np.linalg.det(Ct))
print('Posto controlab =', matrix_rank(Ct))

########################################################
# Matriz de Observabilidade (O)
########################################################
O = ctl.obsv(A, C)
print('Observabilidade: \n', O)
print('det observ =', np.linalg.det(O))
print('Posto observ =', matrix_rank(O))

########################################################
# K
########################################################
pos = np.array([0, 1])
K = pos.dot(Ct_inv).dot(fi_A)
print('K=', K)

