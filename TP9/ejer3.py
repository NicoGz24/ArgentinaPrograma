# Dada una lista de números enteros y un entero k, escribir una función para
# cada uno de los siguientes ítems:
# a- Devuelva tres listas, una con los menores, otra con los mayores y otra con los
# iguales a k.
# b- Devuelva una lista con aquellos que son múltiplos de k.

def tres_en_uno(lista,k):
    listaMayores = []
    listaMenores = []
    listaIguales = []
    for numero in lista:
        if (numero > k):
            listaMayores.append(numero)
        elif(numero < k):
            listaMenores.append(numero)
        else:
            listaIguales.append(numero)
    return listaMayores, listaMenores,listaIguales

def multiplos (lista, k):
    listaMultiplos = []
    for numero in lista:
        if (numero % k == 0):
            listaMultiplos.append(numero)
    return listaMultiplos

lista = [2,3,4,6,29,42,33,54,1,80,97,0,100]
k = 2
mayores,menores,iguales = tres_en_uno(lista,k)
print(f'Los numeros mayores a k de la lista son, {mayores}, los menores son {menores} y los iguales son {iguales}')
print(f'Los multiplos de k de la lista son {multiplos(lista,k)}')
