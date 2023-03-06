# Cree un script que determine si un triángulo es isósceles, equilátero, o
# escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
# números, correspondientes a los tres lados del triángulo.
# equilátero = todos los lados iguales
# isósceles = dos lados iguales
# escaleno = todos los lados diferentes

def determinar_triangulo(lado1,lado2,lado3):
    if(lado1 == lado2) and (lado1 == lado3):
        return 'Triangulo equilátero'
    elif(lado1 != lado2) and (lado1 != lado3):
        return 'Triangulo escaleno'
    return 'Triangulo isósceles'

#Programa principal

lado1 = int(input('Ingrese un lado '))
lado2 = int(input('Ingrese otro lado '))
lado3 = int(input('Ingrese el ultimo lado '))
print('En funcion de los datos ingresados, su figura es un',determinar_triangulo(lado1,lado2,lado3))