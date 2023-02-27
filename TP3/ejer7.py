"""
En Python es posible resolver el problema del intercambio de valores sin
hacer uso de variables adicionales, mediante la sintaxis de asignación
múltiple. Investigue de qué se trata dicha funcionalidad, y utilízela para
resolver el ejercicio anterior sin utilizar variables auxiliares/adicionales.
"""


var1 = 10
var2 = 20
print('Valores originales ', var1,var2)

aux = var1  
var1 = var2
var2 = aux

print('Valores invertidos ',var1, var2)
