
import matplotlib.pyplot as plt
import numpy as np
import math

pi = math.pi
cos = math.cos
sen = math.sin

def curvaComplex1(pontos):
    real1=[]
    imag1=[]
    int=np.linspace(0,pi/2, num=pontos)
    for k in range(pontos):
        real1.append(3*cos(int[k]))
        imag1.append(3*sen(int[k]))

    plt.plot(real1, imag1, 'b', label='Θ ≤ π/2')

def curvaComplex2(pontos):
    real2=[]
    imag2=[]
    int=np.linspace(pi/2,pi, num=pontos)
    for k in range(pontos):
        real2.append(5*cos(int[k]))
        imag2.append(5*sen(int[k]))

    plt.plot(real2, imag2, 'g', label='π/2 < Θ ≤ π')

def curvaComplex3(pontos):
    real3=[]
    imag3=[]
    int=np.linspace(pi,2*pi, num=pontos)
    for k in range(pontos):
        real3.append(-10+5*int[k]/pi)
        imag3.append(0)    

    plt.plot(real3, imag3, 'r', label='π < Θ ≤ 2π')


pontos = 40
curvaComplex1(pontos)
curvaComplex2(pontos)
curvaComplex3(pontos)

plt.title('curva no plano complexo f(Θ)', size=18)
plt.legend()
plt.xlabel('Eixo real', size=13)
plt.ylabel('Eixo imaginário', size=13)
plt.show()
