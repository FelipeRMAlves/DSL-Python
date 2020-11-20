import numpy as np

'''
Recebe 1 polo e retorna:
- Tempo de acomodação;
- Frequencia natural;
- Taxa de amortecimento (ksi);
- Ultrapassagem percentual;
- Tempo de pico


########################################################
Input (Polo)
########################################################
'''
x_s = -3   # real
y_s = 4    # complexo


########################################################
# Codigo
########################################################

Ts = 4/np.absolute(x_s)
wn = np.sqrt(x_s**2 + y_s**2)
teta = np.arctan(np.abs(y_s)/np.abs(x_s))
ksi = np.cos(teta)
UP = np.exp(-ksi*np.pi/(np.sqrt(1-(ksi**2))))*100
wd = wn*(np.sqrt(1-(ksi**2)))
Tp = np.pi/wd

print('T acomodacao = ',round(Ts,3))
print('wn = ', round(wn,3))
print('teta = ', round(teta,3))
print('ksi = ', round(ksi,3))
print('UP = ', round(UP,2), '%')
print('wd = ', round(wd,3))
print('T pico = ',round(Tp,3))
