"""
Modifique la función del ejercicio anterior para que retorne dos versiones del
string recibido como parámetro: primero la versión en minúsculas, y luego la
versión en mayúsculas.
"""

def pasar_a_mayusculas(texto):
    return  texto.lower(),texto.upper()

#Programa principal

cadena = input('Ingrese una cadena de texto ')
enMinusculas,enMayusculas = pasar_a_mayusculas(cadena)
print(enMinusculas)
print(enMayusculas)