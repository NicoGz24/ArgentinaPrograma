# Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
# usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
# el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
# para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.

def leer_palabra():
    return input('Ingrese una palabra ')

#---------------------------------------------------
palabra = leer_palabra()

while (palabra.lower() != 'parar'):
    print(palabra)
    palabra = leer_palabra()
print('-----TERMINADO-----')    