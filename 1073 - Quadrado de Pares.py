numero = int(input())
if (numero%2 == 1):
    numero = numero - 1
cont = 2
while cont <= numero:
    quadrado = cont * cont
    print("{}^2 = {}".format(cont, quadrado))
    cont = cont + 2