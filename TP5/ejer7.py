"""
Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
y retorne True si nombre1 tiene más letras que nombre2, o False en caso
contrario.
"""

def comparCadenas(nombre1,nombre2):
    return (len(nombre1) > len(nombre2))

#Programa principal

nombre1 = input('Ingrese el primero nombre ')
nombre2 = input('Ingrese el segundo nombre ')
print('¿ El primer nombre es mayor que el segundo ?',comparCadenas(nombre1,nombre2))