# Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
# uno, informarle si el mismo es positivo, negativo, o cero.

def tipo_de_numero(numero):
    if(numero > 0):
        tipo = 'Numero positivo'
    elif (numero == 0):
        tipo = 'El numero es cero'
    else:
        tipo = 'Numero negativo'
    return tipo

#-----------------------------------------------------

cantidad = 0
while (cantidad <= 10):
    numero = int(input(f'Ingrese un numero '))
    print('El numero ingresado es', tipo_de_numero(numero))
    cantidad += 1
