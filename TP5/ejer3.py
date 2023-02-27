"""
Cree una función que reciba un string como parámetro, y retorne la cantidad de
letras que posee. Luego, utilice la función para escribir un programa que solicite
ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
ese nombre.
"""

def contarLetras(nombre):
    return len(nombre)

#Programa principal
nombreUsuario = input('Ingresar nombre de usuario ')
print('El usuario',nombreUsuario,'tiene', contarLetras(nombreUsuario),'letras')