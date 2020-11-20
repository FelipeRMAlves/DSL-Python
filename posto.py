import numpy as np
from numpy.linalg import matrix_rank

matriz = [[ 1,  0, 0, 0],
 [0, 0,  1,  0],
 [-4.9, -137, -12,  -2],
 [ 6.220e+03, 2.410e+03 ,  -341.4, -9.5]]
print(matriz)

print('determinante =', np.linalg.det(matriz))
print('Posto da matriz =', matrix_rank(matriz))


