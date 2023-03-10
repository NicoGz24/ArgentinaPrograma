# Un cliente ha solicitado un programa que le permita ingresar los mililitros de
# lluvia caídos diariamente en una semana, para que el programa le informe en
# pantalla el promedio de precipitación de esa semana. El cliente también desea
# saber cuál fue el día en que más llovió en la semana.
# A modo ilustrativo, un reporte generado por el programa debería verse como
# sigue, luego de haber leído las precipitaciones de los 7 días de la semana:

#   El promedio de precipitaciones fue de XX mls. diarios.
#   El día de más precipitaciones fue el xxxxxx (nombre del día).

# Tenga en cuenta que la numeración de los días de la semana comienza con el 1
# para el día domingo.
# Codifique el programa para dar solución a lo solicitado por el cliente.

def dia_semana(numero):
    if (numero == 1):
      return 'Domingo'
    elif(numero == 2):
        return 'Lunes' 
    elif(numero == 3):
       return 'Martes'  
    elif(numero == 4):
        return 'Miercoles'  
    elif(numero == 5):
        return 'Jueves'  
    elif(numero == 6):
        return 'Viernes'  
    else :
        return 'Sabado'  
   

#------------------------------------------------------------------

mxMlDia = 0
promPresipitaciones = 0
diaConMasLluvia = 0
cantidad = 1

while (cantidad <= 7):
    mlDia = int(input('Ingrese las precipitaciones del dia '))
    promPresipitaciones += mlDia
    if ( mlDia > mxMlDia):
        mxMlDia = mlDia
        diaConMasLluvia = cantidad
    cantidad += 1

promPresipitaciones = promPresipitaciones /7
print(f'El promedio de precipitaciones fue de {promPresipitaciones} mls. diarios.')
print(f'El día de más precipitaciones fue el {dia_semana(diaConMasLluvia)}')