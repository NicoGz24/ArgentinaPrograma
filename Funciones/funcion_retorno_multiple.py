
#Definicion de la funcion
def calcular_Permitero_Area_de_Rectangulo(base, altura):
    permimetro = 0 #esto se podria obviar
    area = 0
    permimetro = (base * 2 ) + (altura * 2)
    area = base * altura
    return permimetro,area


#Progama principal
print('Calulador de permitro de una triangulo rectangulo ')
valor1 = int(input('Ingrese la base del triangulo rectangulo ')) #casteo de str a int, los valores por teclado son de tipo caracter, hay que pasarlos a enteros 2
valor2 = int(input('Ingrese la altura del triangulo rectangulo '))
resul1,result2 = calcular_Permitero_Area_de_Rectangulo(valor1, valor2) #se debe respetar el orden de las variables del return en la definicion de la funcion
print('En funcion de los datos ingresados el perimetro es: ', resul1, " y el area es ", result2 )