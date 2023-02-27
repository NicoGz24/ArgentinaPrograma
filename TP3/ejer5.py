"""
Implemente un algoritmo en Python para calcular el área de un rectángulo,
conociendo su base y altura. Los datos se deben almacenar en variables, y el
resultado se debe mostrar en pantalla.
área = base * altura
"""


#Definicion de la funcion
def calcular_Area_de_Rectangulo(base, altura):
    return base * altura


#Progama principal
print('Calulador de permitro de una triangulo rectangulo ')
base = int(input('Ingrese la base del rectangulo ')) #casteo de str a int, los valores por teclado son de tipo caracter, hay que pasarlos a enteros 2
altura = int(input('Ingrese la altura del rectangulo '))
print('En funcion de los datos ingresados el area es ', calcular_Area_de_Rectangulo(base,altura) )