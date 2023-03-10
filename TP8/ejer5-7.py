# Extienda el script del ejercicio anterior para que también informe el número
# mínimo ingresado, y su posición.

maximo = 0
minimo = 0
posMax = 1
posMin = 1
cantidad = 1

while (cantidad <=10):
    numero = int(input('Ingrese un numero '))
    if(numero > maximo):
        maximo = numero     #actualizo el maximo
        posMax = cantidad             #actualizo la pos del nuevo maximo
    if(numero < minimo):
        minimo = numero
        posMin = cantidad
    cantidad += 1
print(f'El numero maximo encontrado es {maximo} en la posicion {posMax}')
print(f'El numero minimo encontrado es {minimo} en la posicion {posMin}')