# Las estructuras alternativas pueden utilizarse para validar datos. Por
# ejemplo, si se intenta crear una función que tome dos enteros como
# parámetro y muestre el resultado de su división, puede ocurrir un error si el
# denominador es cero. Utilice la estructura alternativa para validar que el
# denominador no sea cero; en caso de serlo, la función deberá mostrar el
# mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
# resultado.

def dividir_numeros(num1,num2):
    if(num2 == 0):
        print('No se puede dividir por 0!')
    else:
        print ('El resultado de dividir',num1,'por',num2,'es', num1/num2)

#Programa principal

num1 = int(input('Ingrese un numero '))
num2 = int(input('Ingrese otro numero '))
dividir_numeros(num1,num2)