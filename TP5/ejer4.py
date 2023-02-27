"""
Cree una función que reciba dos números como parámetro (base y exponente),
y retorne el resultado de elevar base a la potencia exponente.
"""

def potencia(base,exponente):
    return base**exponente

#Programa principal

base = int(input('Ingrese la base para calcular la potencia '))
exponente = int(input('Ingrese el exponente para calcular la potencia '))
print('El resultar de elevar la base',base,'al exponente', exponente, 'es',potencia(base,exponente))
