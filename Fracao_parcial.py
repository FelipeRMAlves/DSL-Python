import sympy as sym
from sympy.abc import s,t

# Function
F = (25)/((s) * ((s**2) + 2*s + 25))
print('F =', F)

# Partial fraction decomposition
G = sym.apart(F)
print('G = ', G)