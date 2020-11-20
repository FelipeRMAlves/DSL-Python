import numpy as np

'''
Recebe um valor de S (real e imaginário) e:
- Calcula a magnitude desse S com relacao aos polos e zeros;
- Calcula o angulo desse S com relacao aos polos e zeros.

#############################################################
Input
#############################################################
'''
x_s = 0.0   # real
y_s = 3.2   # complexo
polos = [0, -5, -2]
zeros = []


#############################################################
# Codigo:
#############################################################
M_final = 1.0
ang_final = 0.0

for z in zeros:
    dx = np.absolute(x_s - z)
    dy = y_s
    M = np.sqrt((dx**2) + (dy**2))
    print(f'M(zero {z}) = ', M)
    if dx == 0:
        ang = np.pi/2
    else:
        alfa = np.arctan(dy/dx)
        if x_s >= z:
            ang = alfa
        else:
            ang = np.pi - alfa
    print(f'ang(zero {z}) = ', round((180*ang)/(np.pi),2)) 
    M_final = M_final * M
    ang_final = ang_final + ang

for p in polos:
    dx = np.absolute(x_s - p)
    dy = y_s
    M = np.sqrt((dx**2) + (dy**2))
    print(f'M(polo {p}) = ', M)
    if dx == 0:
        ang = np.pi/2
    else:
        alfa = np.arctan(dy/dx)
        if x_s > p:
            ang = alfa
        elif x_s == alfa:
            ang = np.pi/2
        else:
            ang = np.pi - alfa
    print(f'ang(polo {p}) = ', round((180*ang)/(np.pi),2))
    M_final = M_final / M
    ang_final = ang_final - ang

print('\n')
print('M_final=', M_final)
print('ang_final=', round(ang_final*180/np.pi, 2), 'graus')