# Cree un script que le solicite al usuario ingresar un número por teclado, y le
# informe con un mensaje si su número es positivo, negativo, o 0.

numero = int(input('Ingrese un numero '))
if(numero > 0):
    print('El numero ingresado es positivo')
elif (numero == 0):
    print('El numero ingresado es el cero')
else:
    print('El numero ingresado es negativo')