"""
Cree un script que muestre en pantalla el perímetro de un rectángulo,
leyendo su base y altura desde teclado. perímetro = 2 * (base + altura).
"""


#Progama principal
print('Calulador de permitro de una rectangulo ')
base = int(input('Ingrese la base del rectangulo ')) #casteo de str a int, los valores por teclado son de tipo caracter, hay que pasarlos a enteros 2
altura = int(input('Ingrese la altura del rectangulo '))
permimetro = (base * 2 ) + (altura * 2)
print('En funcion de los datos ingresados el perimetro es: ', permimetro)