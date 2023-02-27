"""
Cree un script que lea dos números de teclado (una base y un exponente)
y luego muestre en pantalla el resultado de elevar el número base a la
potencia exponente.
"""


#Programa principal

print('Calculador de una base elevada a un exponente')
base = int(input('Ingrese la base '))
exponente = int(input('Ingrese el exponente '))
print('El resultado de elevar la base ',base,' al exponente ',exponente, ' es = ', (base**exponente))