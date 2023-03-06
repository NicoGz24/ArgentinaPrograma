# Modifique el script anterior para que mantenga el funcionamiento, pero
# ahora, cuando el número no es mayor que 10, también se muestre un
# mensaje “Tu número (N) es menor o igual que 10!”.

numero = int(input('Ingrese un numero '))
if(numero > 10):
    print('Tu numero',numero,'es mayor a 10')
else:
    print('Tu numero',numero,'es menor o igual a 10')
print('Saludos!')