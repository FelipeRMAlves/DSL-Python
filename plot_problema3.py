from numpy import *
import math
import matplotlib.pyplot as plt

# input:
a_const = 4
a_elev = -2
b_const = -2
b_elev = -1
c_const = 0
c_elev = -1
intervalo = 10  # de zero a dez

t = linspace(0, intervalo, 400)

a = a_const * exp((a_elev)*t)
b = b_const * exp((b_elev)*t)
c = c_const * exp((c_elev)*t)
d = a + b + c

ax = plt.axes()
ax.set_xlabel('tempo', fontsize=14)
ax.set_ylabel('f(t)', fontsize=14)
plt.title(f'Problema 3(c)', fontsize=16)
plt.plot(t, d, 'g')
plt.show()