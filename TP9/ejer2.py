# Dada una lista de números enteros, escribir una función para cada uno de los
# siguientes ítems:
# a- Devuelva una lista con todos los números que sean primos.
# b- Devuelva la sumatoria y el promedio de los valores.
# c- Devuelva una lista con el factorial de cada uno de esos números.
def es_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos(lista):
    resultado = []
    for numero in lista:
        if es_primo(numero):
            resultado.append(numero)
    return resultado

def sumatoria_promedio(lista):
    sumatoria = 0
    promedio = 0
    for numero in lista:
        sumatoria += numero
    promedio = sumatoria / len(lista)
    return sumatoria, round(promedio,2)

def factorial(lista):
    lista_factorial = []
    for numero in lista:
        factorial = 1
        for i in range(1,numero+1):  
            factorial = factorial * i
        lista_factorial.append(factorial)
    return lista_factorial

lista = [1,2,5,7,8,10,22,23,55]
print(f'Los numeros primos de la lista son {numeros_primos(lista)}')
sumatoria,promedio = sumatoria_promedio(lista)
print(f'La sumatoria de los elementos es {sumatoria} y el promedio es {promedio}')
print(f'El factorial de los elementos de la lista es f{factorial(lista)}')