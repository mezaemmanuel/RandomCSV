import random
import csv
import time
from datetime import datetime
from datetime import date
from time import time
import os
import shutil
import asyncio

DateNow = date.today()
TimeNow = datetime.now().time()
now = datetime.now()
CurentHour = TimeNow.hour

filename = str(DateNow) + ".csv"
directorio = 'D:\Pruebas\Pruebas Monitor M/' + str(DateNow)
if os.path.isdir(directorio): #ESTA COMPROBACION NOS AYUDA A QUE SI EL PROGRAMA SE NOS TRUNCO Y VUELVE 
#ARRANCAR NO SE BOTE POR QUE LA CARPETA YA EXISTE
    print('La carpeta existe. Corriendo programa...')

else:
    os.mkdir(directorio)
    print('La carpeta no existia.'); # EN CASO DE NO EXISTIR LA CREARA.
# Nombre del archivo CSV a crear
dirfilename = directorio + '/' + filename #AHORA VIENE LA CREACION DEL ARCHIVO. DENTRO DE LA CARPETA CREADA.
print (filename)

# Encabezados de las columnas en el archivo CSV
headers = ['F/H', 'VFD', 'F', 'P', 'AMP_M1', 'AMP_M2', 'R1', 'R2', 'G1', 'G2', 'UM1', 'F', 'P', 'AMP_M1', 'AMP_M2', 'R1', 'R2', 'G1', 'G2', 'UM2', 'NIVEL DE LECHE']

# Horas de inicio y finalización del programa
start_hour = 9
end_hour = 17

# Función para escribir el número aleatorio en el archivo CSV
async def write_random_num():
    # Verificar si la hora actual está dentro del rango de horas especificado
    current_hour = int(datetime.now().strftime('%H'))
    if current_hour >= start_hour and current_hour < end_hour:
        #Variables y Randoms para Archivo CSV 
        VFD = 'ON'
        F = 2048
        P = 87
        AMP_M1 = random.randint(122, 211)
        AMP_M2 = random.randint(13652, 13746)
        R1 = 'OK'   
        R2 = 'OK'
        G1 = 'OK'
        G2 = 'OK'
        UM1 = 'Inactiva'
        F1 = random.randint(72, 97)
        P1 = 246
        AMP_M12 = random.randint(1035, 1277)
        AMP_M22 = random.randint(1006, 1172)
        R11 = 'FALLA'
        UM2 = 'ACTIVA'
        Nivel = 24900
        # Obtener la hora actual
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Escribir el número aleatorio y la marca de tiempo en el archivo CSV
        with open(dirfilename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, VFD, F, P,AMP_M1, AMP_M2, R1, R2, G1, G2, UM1, F1, P1, AMP_M12, AMP_M22, R11, R2, G1, G2, UM2, Nivel])
    else:
        print("No está dentro del horario permitido.")

    # Esperar 4 segundos antes de generar y escribir el siguiente número aleatorio
    await asyncio.sleep(4)

# Función principal del programa
async def main():
    # Abrir el archivo CSV en modo de escritura y escribir los encabezados de las columnas
    with open(dirfilename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    # Generar y escribir un número aleatorio en el archivo CSV cada 4 segundos
    while True:
        await write_random_num()

# Ejecutar el programa
if __name__ == '__main__':
    asyncio.run(main())