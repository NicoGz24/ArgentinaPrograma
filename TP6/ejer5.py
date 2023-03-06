# Cree un script que, dado un número de día de la semana ingresado por
# teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
# números y días de la semana es la siguiente:
# 1 = Domingo.
# 2 = Lunes.
# 3 = Martes.
# 4 = Miércoles.
# 5 = Jueves.
# 6 = Viernes.
# 7 = Sábado.

dia = int(input('Ingrese la opcion deseada del 1 al 7 '))
cadena = 'El dia elegido es el '

if(dia == 1):
    cadena += 'domingo'
elif(dia == 2):
    cadena += 'lunes'
elif(dia == 3):
    cadena += 'martes'
elif(dia == 4):
    cadena += 'miercoles'
elif(dia == 5):
    cadena += 'jueves'
elif(dia == 6):
    cadena += 'viernes'
elif(dia == 7):
    cadena += 'sabado'
else:
    cadena = 'La opciones ingresada no es valida'
print(cadena)