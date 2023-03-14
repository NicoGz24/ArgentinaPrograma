# Modificar el ejercicio anterior para que en lugar de devolver una nueva lista,
# modifique la lista dada para invertirla. Usar listas auxiliares.

lista = ['Di', 'buen', 'día', 'a', 'papa']
print(f'Lista original {lista}')
#Para mi que no pide esto pero yo lo asi xq tengo muchos eggs
auxiliar = lista[::-1]
lista = auxiliar
print(f'La lista invertida es {lista}')