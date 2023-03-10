# Vuelva a construir el menú del ejercicio 6 del Trabajo Práctico VI, pero esta vez
# agregue una nueva opción llamada “Salir”. El programa deberá mostrar el menú
# y reaccionar a la opción seleccionada por el usuario, pero ahora, al ejecutar una
# opción, en vez de terminar el programa, se mostrará nuevamente el menú,
# hasta que el usuario seleccione la opción 4. Salir.

# ********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir.
# Seleccione una opción [1-4]:

import os


def menu ():
    print('********* MI PROGRAMA *********')
    print('1. Saludar')
    print('2. Informar temperatura.')
    print('3. Mostrar nombre de materia.')
    print('4. Salir.')
    return input('Seleccione una opción [1-4]: ')
#-------------------------------------------------------------

opcion = menu()
while (opcion != '4'):
    if(opcion == '1'):
        print('Hola wachin')
    elif(opcion == '2'):
        print('32 grados celsius')
    else:
        print('Introducción a la Programación')
    input('PRESIONE ENTER PARA CONTINUAR')
    os.system('cls')
    opcion = menu()

