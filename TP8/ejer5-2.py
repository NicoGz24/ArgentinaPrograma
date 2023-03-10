# Modifique el script del ejercicio anterior para que se muestren sólo los números
# pares. Para saber si un número es par, utilice el operador de módulo (%).

num = 1

while (num <= 100):
    if(num % 2 == 0):
        print(num)
    num += 1