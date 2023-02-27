"""
Cree un script que almacene un número entero en una variable, y luego
muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N
es |N|”. Finalmente, verifique que su programa funciona correctamente,
ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego
con el valor -10 (la salida debería ser 10 nuevamente).
"""

def valor_absoluto(numero):
    return abs(numero)
 


valor= int(input('Ingrese un numero '))
print('El valor absoluto del numero ingresado es: ', valor_absoluto(valor))

