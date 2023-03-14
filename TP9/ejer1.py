# Diseñe una función que reciba una lista, vacía o no, e incorpore números hasta que
# el usuario ingrese el valor “salir”. Cuando termina de ingresar los datos, la
# función debe retornar la lista al programa principal.

def pedir_numero():
    return input('Ingrese un numero ')

def guardar_numeros(lista):
    valor = pedir_numero()
    while(valor.lower() != 'salir'):
        if (valor.isdigit()):
            lista.append(valor)
        valor = pedir_numero()
    return lista

lista = []
lista = guardar_numeros(lista)
for elemento in lista:
    print(elemento)        
