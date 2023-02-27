"""
Escriba un algoritmo que, conociendo las notas de los dos parciales de un
alumno de la asignatura Introducción a la Programación, muestre en
pantalla su promedio.
"""
def calcularPromedio(nota1,nota2):
    return (nota1+nota2)/2


nota1 = 9
nota2 = 5
print('El promedio de las notas del alumno es: ',calcularPromedio(nota1,nota2))