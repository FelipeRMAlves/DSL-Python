import numpy as np
import control.matlab as ctl
import matplotlib.pyplot as plt

'''
Recebe os coefs da funcao de transferencia e:
- Plota o grafico de Bode

#############################################################
Input (coefs funcao de transferencia)
#############################################################
'''
num = [0.003226, 0.03458, 1.615]
den = [1, 21, 976.4, 8351, 164400]


#############################################################
# Codigo:
#############################################################
H = ctl.tf(num, den)
print(H)
w0 = 0.1
w1 = 100
dw = 0.001
nw = int((w1 - w0) / dw) + 1   # Number of points of freq
w = np.linspace(w0, w1, nw)
(mag, phase_rad, w) = ctl.bode(H, dB=True, Hz=False)
plt.title('Diagrama de bode para G1 (x)',pad=155)
plt.show()


# plt.polar(phase_rad*180/np.pi, mag, 'r.')
# plt.show()
