"""
Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
un string cualquiera, y luego lo retorne. 

Luego cree otro archivo llamado programa_principal.py, que ejecute el programa haciendo uso de la función
creada en el otro archivo.
"""
import modulo_cadena

cadena = modulo_cadena.leer_cadena()
print('Cadena en mayusculas', cadena.upper())