#####################################################
# MS211C - Cálculo Numérico
# Método Euler Modificado
# Nome: Gabriel Henrique Cerqueira
# RA: 197356
#####################################################

# Importar o que e preciso
import numpy as np
import math
import matplotlib.pyplot as plt

# Função de y'
def y_linha(y, x):
    valor = y/x - (y/x)**2
    return valor

# Contas
h = 0.1
y_inicial = 1
lista_de_valores = []
lista_de_x = []
x = 1

while (x <= 2 and 1 <= x):
    k_um = y_linha(y_inicial, 1)
    k_dois = y_linha(y_inicial + k_um*h, x + h)
    k_novo = 1/2 * (k_um + k_dois)
    y_novo = y_inicial + k_novo*h
    lista_de_valores.append(y_novo)
    lista_de_x.append(x)
    y_inicial = y_novo
    x = x + h

print (lista_de_valores)
plt.plot(lista_de_x,lista_de_valores)
plt.xlabel('valores de x')
plt.ylabel('valores de y')
plt.grid(alpha=.4,linestyle='--')
plt.show()
