#####################################################
# MS211C - Cálculo Numérico
# Método de Newton 
# Nome: Gabriel Henrique Cerqueira
# RA: 197356
#####################################################

  
# Importar o que e preciso
import numpy as np
import math 

# Parte (0) - Equacoes
def F_x_valor_total (x_1, x_2, x_3):
    f_1 = 3*x_1 - math.cos(((x_2*math.pi)/180)*((x_3*math.pi)/180)) - 0.5
    f_2 = x_1**2 - 81*(x_2 + 0.1)**2 + math.sin((x_3*math.pi)/180) + 1.06
    f_3 = math.e**(-x_1*x_2) + 20*x_3 + (10*math.pi - 3)/3
    saida = (f_1**2 + f_2**2 + f_3**2)**(1/2)
    return saida

def F_x_matriz (x_1, x_2, x_3):
    f_1 = 3*x_1 - math.cos(((x_2*math.pi)/180)*((x_3*math.pi)/180)) - 0.5
    f_2 = x_1**2 - 81*(x_2 + 0.1)**2 + math.sin((x_3*math.pi)/180) + 1.06
    f_3 = math.e**(-x_1*x_2) + 20*x_3 + (10*math.pi - 3)/3
    matriz = [[f_1], [f_2], [f_3]]
    return matriz

def jacobiano(x_1, x_2, x_3):
    jacob = [[3, x_3*math.sin((x_2*math.pi)/180), x_2*math.sin((x_3*math.pi)/180)], 
    [2*x_1, -162*(x_2 + 0.1), math.cos((x_3*math.pi)/180)],
    [-x_1*math.e**(-x_1*x_2), -x_2*math.e**(-x_1*x_2), 20]]
    return jacob

# Parte (1) - Entrada
k = 0
erro = 10**(-5)
x_1 = float(input())
x_2 = float(input())
x_3 = float(input())
s = []
x_zao = [[x_1], [x_2], [x_3]]

# Parte (2) - Aplicacao
fx = F_x_valor_total(x_1, x_2, x_3)
valor_distancia = 1
while (fx > erro) and ((valor_distancia) > erro):
    A = np.linalg.inv(np.matrix(jacobiano(x_1, x_2, x_3)))
    B = F_x_matriz(x_1, x_2, x_3)
    C = [[-1 * B[0][0]], [-1 * B[1][0]], [-1 * B[2][0]]]
    s = A @ C
    x_novo = s + x_zao
    distancia = x_novo - x_zao
    valor_distancia = ((float(distancia[0][0]))**(2) + (float(distancia[1][0]))**(2) + (float(distancia[2][0]))**(2)) ** (1/2)
    x_zao = x_novo
    x_1 = float(x_zao[0][0])
    x_2 = float(x_zao[1][0])
    x_3 = float(x_zao[2][0])
    fx = F_x_valor_total(x_1, x_2, x_3)
    print(valor_distancia)
    print (fx)
    k += 1
    print (k)
    print (x_1, x_2, x_3)

print ("acabou e deu bom")



