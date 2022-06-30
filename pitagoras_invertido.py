N = int(input())
 
numero = 0
lista = []
listinha = []
valores_a = []
valores_b = []
valores_c = []
alerta_a = 0
alerta_b = 0
alerta_c = 0
for i in range (N, 1, -1):
    c = i
    for j in range (c, 1, -1):
        b = j
        a = (c**2 - b**2)**(1/2)
        alerta_a = 0
        alerta_b = 0
        alerta_c = 0
        if (a > 0):
            for k in valores_a:
                if a%k == 0:
                    alerta_a = 1
            for l in valores_b:
                if (b%l == 0):
                    alerta_b = 1
            for g in valores_c:
                if c%g == 0:
                    alerta_c = 1    
            if ((alerta_c != 1)  and (alerta_b != 1) and (alerta_a != 1)):     
                if (a%1 == 0) and ((a and b) not in valores_a):
                    valores_a.append(a)
                    valores_b.append(b)
                    valores_c.append(c)
                    #listinha = [int(a), b, c]
                    numero = numero + 1    
                    #lista.append(listinha)
print (numero)
#print (lista)
