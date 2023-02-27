
#Definicion de la funcion
def calcularPermitero(base, altura):
    permimetro = 0
    permimetro = (base * 2 ) + (altura * 2)
    return permimetro


#Progama principal
print('Calulador de permitro de una triangulo rectangulo ')
valor1 = int(input('Ingrese la base del triangulo rectangulo ')) #casteo de str a int, los valores por teclado son de tipo caracter, hay que pasarlos a enteros 2
valor2 = int(input('Ingrese la altura del triangulo rectangulo '))
print('En funcion de los datos ingresados el perimetro es: ', calcularPermitero(valor1,valor2))