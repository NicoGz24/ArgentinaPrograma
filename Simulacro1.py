
"""
Realice las funciones solicitadas a continuación
No cambie los nombres de las funciones
Ninguna función necesita ingreso por teclado
por lo cual ninguna lleva la instrucción "input"

El archivo se debe guarda con el nombre:
    DNIxxxxxxxx.py
Donde DNI va con MAYÚSCULAS y xxxxxxxx debe ser su Nro de DNI

"""

"""
Realice una función que reciba 2 números enteros distintos y 
retorne el mayor de los números elevado al menor.
"""
def potencia(a,b): #No cambiar este encabezado
   return a**b

print (f'El resultado de calcular la potencia de 2 elevado al exponente 3 es {potencia(2,3)}')

"""
Realice una función que reciba el importe de un pedido hecho y devuelva 
lo que debo pagar cuando llegue teniendo en cuenta que el
envio cuesta un 10% de la compra - Si corresponde redondear en 2 decimales
"""
def pagoPropina(importe): #No cambiar este encabezado
    return round(importe + (importe * 0.10),2)


print(f'El pago de su pedido con el envio incluido es de {pagoPropina(123.567)}')

"""
Realice una función que reciba dos números como parámetro y retorne
la sumatoria de todos los números que existen entre ellos, incluidos estos dos.
Por ejemplo:
 - Si los números ingresados son 3 y 7 deberá retornar 25.
 - Si los números ingresados son 5 y 1 deberá retornar 15.

"""
def sumatoria(n1, n2): #No cambiar este encabezado
    max = 0
    min = 0
    if(n1 > n2):
        max = n1
        min = n2
    else:
        max = n2
        min = n1
    suma = 0
    for i in range(min,max+1):
        suma += i
    return suma

print(f'La sumatoria desde 3 a 7 es = {sumatoria(3,7)}')
print(f'La sumatoria desde 5 a 1 es = {sumatoria(5,1)}')
    


'''
Realice una función que reciba dos strings distintos y retorne el string mas corto
'''

def string_corto(a,b):
    if (len(a) > len(b)):
        return b
    else:
        return a
    
largo = 'pedriño'
corto = 'pedro'
print(f'El string mas corto entre {largo} y {corto} es {string_corto(largo,corto)}')



