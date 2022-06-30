#####################################################
# MS211C - Cálculo Numérico
# MMQ
# Nome: Gabriel Henrique Cerqueira
# RA: 197356
#####################################################

# Importar o que e preciso
import numpy as np
import math
import matplotlib.pyplot as plt

dados_y = [np.log(30), np.log(10), np.log(9), np.log(6), np.log(5), np.log(4), np.log(4)]
dados_x = [-8, -6, -4, -2, 0, 2, 4]
soma = 0
quadrado = 0
for x in dados_x:
    soma = soma +  x
    quadrado = quadrado + x**2
print (quadrado)    
print(soma)
somy = 0
for y in dados_y:
    somy = somy + y
print (somy)
somona = 0
for i in range(len(dados_x)):
    somona = somona + dados_x[i]*dados_y[i]
print(somona)
A = np.array([[len(dados_y), soma], [soma, quadrado]])
B = np.array([somy, somona])
resultado = np.linalg.solve(A, B)
print (resultado)
f_1 = (math.exp(resultado[0]))
f_2 = (math.exp(resultado[0]) * math.exp(resultado[1]))

y_plotavel = [f_1, f_2]
x_plotavel = [0, 1]

nova_soma = 0
for i in range(len(dados_x)):
    nova_soma = nova_soma + (math.exp(resultado[0]) * (math.exp(resultado[1]))**dados_x[i]) - dados_y[i]
dp = 0
dp = (nova_soma/(len(dados_x)))**(1/2)
print(dp)

plt.plot(x_plotavel, y_plotavel)
plt.xlabel('valores de dados_x')
plt.ylabel('valores de dados_y')
plt.grid(alpha=.4,linestyle='--')
plt.show()

plt.plot(dados_x, dados_y)
plt.xlabel('valores de dados_x')
plt.ylabel('valores de dados_y')
plt.grid(alpha=.4,linestyle='--')
plt.show()
