# Cree un script que le solicite al usuario ingresar un número por teclado, y
# luego le informe en pantalla si su número es mayor que 10; antes de finalizar
# e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:

numero = int(input('Ingrese un numero '))
if(numero > 10):
    print('Tu numero',numero,'es mayor a 10')
print('Saludos!')