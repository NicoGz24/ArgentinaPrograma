# Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
# hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
# cargar. Una vez ingresadas las notas, el programa debe informar la nota
# promedio (tenga cuidado de no incluir al -1 dentro del promedio).

def leer_nota():
    return int(input('Ingrese la nota de su parcial '))

#-------------------------------------------------------

nota = leer_nota()
notas = 0
cantidad = 0

while (nota != -1):
    notas += nota
    cantidad += 1
    nota = leer_nota()
print(f'El promedio de sus notas es igual a {notas/cantidad}')