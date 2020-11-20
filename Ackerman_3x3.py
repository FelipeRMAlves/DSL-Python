import numpy as np
import control.matlab as ctl
from scipy.signal import tf2ss

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
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [-30, -31, -10]])
B = np.array([[0], 
              [0],
              [1]])
C = np.array([0, 0, 1])
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
poles = [-2+4j, -2-4j, -10]


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
alfa3 = 200
# alfa4 = 0

A2 = np.matmul(A, A)     # Matriz A^2
A3 = np.matmul(A2, A)    # Matriz A^3
# A4 = np.matmul(A3, A)    # Matriz A^4
print('A2: \n', A2)
print('A3: \n', A3)

# fi_A:
fi_A = A3 + alfa1*A2 + alfa2*A + alfa3*np.identity(3)
print('fi(A): \n', fi_A)


########################################################
# Matriz de controlabilidade (C)
########################################################
Ct = ctl.ctrb(A, B)
Ct_inv = np.linalg.inv(Ct)
print('Controlabilidade: \n', Ct)
print('Controlabilidade^-1: \n', Ct_inv)


########################################################
# Matriz de Observabilidade (O)
########################################################
# O = ctl.obsv(A, C)
# print('Observabilidade: \n', O)


########################################################
# K
########################################################
pos = np.array([0, 0, 1])
K = pos.dot(Ct_inv).dot(fi_A)
print('K=', K)

