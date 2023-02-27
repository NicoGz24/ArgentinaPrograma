"""
Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
ahorrada en su cuenta (almacenando ese monto en una variable), muestre
en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
$14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
formato:
"""

ahorrosPesos = 5000
valorDolar = 80.5
valorReal = 14.1
valorEuro = 69.5
print('Usted tiene $',ahorrosPesos,'pesos argentinos, los cuales se convertiran en')
print(int(ahorrosPesos / valorDolar), 'dolares')
print(int(ahorrosPesos / valorReal), 'reales')
print(int(ahorrosPesos / valorEuro), 'euros')
