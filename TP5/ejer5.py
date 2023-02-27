"""
Cree una función que reciba un string como parámetro, y retorne el mismo
string, pero con todas las letras convertidas a mayúsculas.
"""

def pasar_a_mayusculas(texto):
    return  texto.upper()

#Programa principal

cadena = input('Ingrese una cadena de texto ')
print(pasar_a_mayusculas(cadena))