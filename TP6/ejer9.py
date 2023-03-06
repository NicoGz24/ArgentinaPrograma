# Python ofrece algunas funciones built-in para facilitar la implementación de
# validaciones. A continuación se listan algunas de las más comunes:
# valor.isdigit()
# Retorna True si todos los caracteres de valor son numéricos, False en caso
# contrario.
# valor.isalpha()
# Retorna True si todos los caracteres de valor son alfabéticos (no
# numéricos), False en caso contrario.
# valor.isalnum()
# Retorna True si valor es una combinación alfanumérica (caracteres y
# números), False en caso contrario.
# Codifique una función que reciba un parámetro cualquiera proveniente del
# usuario del programa (que puede contener letras, números, o una combinación
# de ambas), e indique si el mismo es un número, una palabra, o un valor
# alfanumérico. Compruebe que su función resuelve el problema enviándole
# valores correspondientes a las tres posibilidades.

def validar_entrada(cadena):
    if(cadena.isdigit()):
        return 'La cadena ingresada es numerica'
    elif(cadena.isalpha()):
        return 'La cadena ingresada es alfabética'
    elif(cadena.isalnum()):
        return 'La cadena ingresada es alfanumérica' 
    return 'La cadena ingresada posee caracteres especiales o espacios en blanco'

#Programa principal

cadena = input('Ingrese lo que desea validar ')
print(validar_entrada(cadena))
