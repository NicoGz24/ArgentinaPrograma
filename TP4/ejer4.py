"""
Cree un script que le solicite a un alumno ingresar su apellido, la nota del
primer parcial, y la nota del segundo parcial. Finalmente, se debe mostrar
un reporte con la siguiente información:
"""

apellido = input('Ingrese su apellido ')
nota1 = int(input('Ingrese la nota de su primer parcial '))
nota2 = int(input('Ingrese la nota de su segundo parcial '))
promedio = (nota1+nota2)/2

print('Alumno: ',apellido)
print('Primer parcial: ',nota1)
print('Segundo parcial: ',nota2)
print('Promedio: ',promedio)