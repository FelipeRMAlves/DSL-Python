
import control as ctl
import numpy as np

'''
Recebe funcao de transferencia e:
- Retorna espaco de estados

#############################################################
Input (numerador e denominador da funcao de transferencia)
#############################################################
# entre com os coeficientes do numerador e denominador
# exemplo Nise 3.5 (pag 207 PDF):
# G(S) = (s^2 + 7s + 2)/(s^3 + 9s^2 + 26s + 24)
'''
num = [1, 7, 2]
den = [1, 9, 26, 24]
G = ctl.tf(num, den)
print('G =', G)


########################################################
#  Espaco de estados
########################################################
S = ctl.tf2ss(G)
print('S:\n', S)
