import funcion_retorno_multiple



#Progama principal
def main():
    print('Calulador de permitro de una triangulo rectangulo ')
    valor1 = int(input('Ingrese la base del triangulo rectangulo ')) #casteo de str a int, los valores por teclado son de tipo caracter, hay que pasarlos a enteros 2
    valor2 = int(input('Ingrese la altura del triangulo rectangulo '))
    """
    Para usar las funcion del modulo importado se debe utilizar el nombre del mismo y luego, separado por un . la funcion que se quiere usar
    """
    resul1,result2 = funcion_retorno_multiple.calcular_Permitero_Area_de_Rectangulo(valor1, valor2) #se debe respetar el orden de las variables del return en la definicion de la funcion
    print('En funcion de los datos ingresados el perimetro es: ', resul1, " y el area es ", result2 )

main()