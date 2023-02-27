"""
Modifique el script del ejercicio anterior para que la función retorne el resultado
en vez de mostrarlo. El programa debe seguir mostrando el resultado en
pantalla.
"""

def suma(num1, num2):
   return num1+num2

#Programa principal

num1 = int(input('Ingrese el primer numero '))
num2 = int(input('Ingrese el segundo numero '))
print('La suma de los numeros ingresados es: ',suma(num1,num2))