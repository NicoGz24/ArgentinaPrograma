# Realizar una función que, dada una lista, devuelva una nueva lista cuyo
# contenido sea igual a la original pero invertida:
# Ejemplo: L1=['Di', 'buen', 'día', 'a', 'papa'] devolverá ['papa', 'a', 'día', 'buen', 'Di']


def invertir_lista(lista):
    aux = lista[::-1]
    return aux

lista = ['Di', 'buen', 'día', 'a', 'papa']
print(f'Lista original {lista}')
print(f'La lista invertida es {invertir_lista(lista)}')