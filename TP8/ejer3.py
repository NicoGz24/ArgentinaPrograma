# Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
# programa debe ser capaz de solicitarle al usuario que reingrese el número
# cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
# vez que detecte un error de validación, informele al usuario cuál fue el error, con
# los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
# fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
# válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.

def validar_numero(numero):
    while (not numero.isdigit()):
        numero = input('El numero ingresado no es un digito, pruebe nuevamente ')
    return int(numero)
#------------------------------------------------------------------------------------------

numero = input('Ingrese un numero ')
numero = validar_numero(numero)

while (numero < 1) or (numero > 100):
    numero = input ('Numero fuera de rango, vuelva a ingresar a otro numero ')
    numero = validar_numero(numero)


print(numero,'VALIDO')