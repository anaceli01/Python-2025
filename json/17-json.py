import json
import os

ruta = os.path.join('json', 'datos.json') #ruta relativa => json/datos.json

#LECTURA DEL ARCHIVO JSON
print('=====LECTURA DEL ARCHIVO JSON=====')

#utf-8 ES EL ENCODING PARA TRABAJAR IDIOMA ESPAÑOL
#LA  LETRA 'r' ES DE read = lectura
with open(ruta, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo) #Conversión de JSON a una estructura Python

#MOSTRAR LOS USUARIOS DEL ARCHIVO JSON
for usuario in datos:
    print(f'ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}')

#ESCRITURA DEL ARCHIVO JSON
print('=====ESCRITURA DE JSON=====')


#AGREGAR UN NUEVO USUARIO

nuevo_usuario = {
    'id' : 5,
    'nombre' : 'Fernanda',
    'edad' : 30
}

datos.append(nuevo_usuario)

#GUARDAR LOS CAMBIOS EN EL ARCHIVO JSON UTILIZANDO json.dump()
# w : write = escribir

with open(ruta, 'w', encoding='utf-8') as archivo:
    json.dump(
        datos,
        archivo,
        indent=4
    )