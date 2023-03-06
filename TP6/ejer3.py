# Cree un script que le solicite al usuario ingresar dos números por teclado, y
# luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
# de que los números sean iguales, y muestre un mensaje acorde.

numero1 = int(input('Ingrese un numero '))
numero2 = int(input('Ingrese otro numero '))
if(numero1 > numero2):
    print('El numero',numero1,'es mayor que el',numero2)
elif (numero2 > numero1):
    print('El numero',numero2,'es mayor que el',numero1)
else:
    print('Los numeros ingresados son iguales')
