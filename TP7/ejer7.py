# Extienda el script del ejercicio anterior para que también informe el número
# mínimo ingresado, y su posición.


maximo = 0
minimo = 0
posMax = 1
posMin = 1

for i in range(1, 11):
    numero = int(input('Ingrese un numero '))
    if(numero > maximo):
        maximo = numero     #actualizo el maximo
        posMax = i             #actualizo la pos del nuevo maximo
    if(numero < minimo):
        minimo = numero
        posMin = i
print(f'El numero maximo encontrado es {maximo} en la posicion {posMax}')
print(f'El numero minimo encontrado es {minimo} en la posicion {posMin}')