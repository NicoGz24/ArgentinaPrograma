# Cree un script que le solicite al usuario ingresar un número entero, y muestre
# en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
# este ejercicio, pero recuerde que la función range no incluye al valor máximo
# enviado como parámetro.
# factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n

def factorial (numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial = factorial * i
    return factorial

numero = int(input('Ingrese el numero para calcular el factorial '))
print('El resultado de',numero,'! es',factorial(numero))