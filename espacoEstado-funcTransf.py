
import control as ctl
import numpy as np

'''
Recebe espaco de estados:
- Retorna funcao de transferencia

#############################################################
Input (Matrizes espaco de estados)
#############################################################
'''
A = np.array([[0, 0, 1, 0], 
              [0, 0, 0, 1], 
              [-490, -137, -12, -2], 
              [-170, -383, -2.3, -9]])
B = np.array([[0], 
              [0], 
              [1000/310], 
              [-693/250]])
C = np.array([[1, 0, 0, 0]])
D = np.array([[0]])

S = ctl.ss(A, B, C, D)
print('S: \n', S)


#########################################################
#  Funcao de transferencia
#########################################################
G = ctl.ss2tf(S)
print('G =', G)

