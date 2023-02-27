"""
Cree una función que reciba dos números como parámetro, y muestre en
pantalla la suma aritmética de ambos. Invoque a la función con dos números
leídos desde teclado.
"""

def suma(num1, num2):
    print('La suma de los numeros ingresados es: ',num1+num2)

#Programa principal

num1 = int(input('Ingrese el primer numero '))
num2 = int(input('Ingrese el segundo numero '))
suma(num1,num2)