"""
Implemente un algoritmo que intercambie los valores entre dos variables a y
b cualesquiera. Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la
variable a debería ser igual 5, y la variable b debería ser igual a 10.
"""

var1 = 10
var2 = 20
print('Valores originales ', var1,var2)

aux = var1  
var1 = var2
var2 = aux

print('Valores invertidos ',var1, var2)