
# Cree un script que almacene su nombre de pila en una variable, y luego
# muestre en pantalla la cantidad de letras de ese nombre, con el mensaje “El
# nombre [NOMBRE] tiene [N] letras.”.


def calcular_cantidad_letras(nombre):
    return len(nombre)


#Programa principal

nombre = input('Ingrese su nombre de pila ')
print("El nombre ", nombre, "tiene ", calcular_cantidad_letras(nombre), " letras.")