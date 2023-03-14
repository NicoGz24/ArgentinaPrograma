# Escribir una función que reciba una cadena a buscar y una lista de nombres
# de personas y busque dentro de la lista, todas los elementos que contengan esa
# cadena o cualquier parte de ella. Debe devolver una lista con los elementos
# encontrados.

def buscar_cadena (cadena, lista):
    encontrados = []
    for nombre in lista:
        if(cadena.lower() in nombre.lower()):
            encontrados.append(nombre)
    return encontrados

lista = ['hola_mundo','pedro','ruben','mundiño','mundito','mundo_marino','agustina','el_mundo_de_boby']
cadena = 'mundo'
print(f'Los elementos de la lista que contienen el string {cadena} son {buscar_cadena(cadena,lista)}')