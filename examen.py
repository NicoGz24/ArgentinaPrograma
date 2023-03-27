# Escribir una función que reciba dos números enteros positivos y
# retorne su suma invertida. Ayuda un int se puede pasar a str y viceversa 
# Ejemplo, si recibe (123,456) (123+456=579), Retornaría 975.
# OJO retorna un ENTERO

def invertir_numero(numero1,numero2):
    suma = numero1 + numero2
    resultado = str(suma)
    suma = resultado[::-1]
    return int(suma)

# Escribir una función que reciba un número entero y devuelva FALSE si el 
# número es igual a la suma de sus divisores sin contarse a el mismo.
# Y TRUE en caso contrario 
# Ejemplo, 6 Retornaría FALSE porque 1 + 2 + 3 = 6.
# Ejemplo, 8 Retornaría TRUE porque 1 + 2 + 4 != 8.

def es_numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if (numero % i == 0):
            suma += i
    if (suma == numero):
        return False
    else:
        return True

# Escribir una función que reciba una lista de números enteros y además 
# un número entero n, y devuelva una lista con los números que 
# son mayores a n en el mismo orden que aparecen.
# Ejemplo ([3,6,2,4,7,1,8],6) retornaría [7,8]
# Ejemplo ([3,6,2,4,7,1,8],3) retornaría [6,4,7,8]

def numeros_mayores(lista, n):
    listaResul =[]
    for numero in lista:
        if(numero > n):
            listaResul.append(numero)
    return listaResul

# Escribir una función que reciba una lista de números enteros positivos
# entre los que hay un -1 (menos uno) y retorne el promedio de los valores
# de la lista hasta el valor -1 (redondeado a 2 decimales).
# EJEMPLO: lista = [8, 12, 9, -1, 7, 20] retornaría 9.67 
# EJEMPLO: lista = [4, 6, 2, 1, -1, 13, 12, 20] retornaría 3.25
# EJEMPLO: lista = [5, 3, 7, 9, 10, 4, -1, 6] retornaría 6.33

def promedio(lista):
    i=0
    suma = 0
    while(lista[i] != -1):
        suma += lista[i]
        i+=1
    return round((suma/i),2)

