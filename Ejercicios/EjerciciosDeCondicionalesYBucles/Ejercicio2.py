
#PEDIR LA CANTIDAD DE ALUMNOS
cant_alumnos = int(input('Ingrese la cantidad de alumnos: \n'))


#EN CASO DE ERROR, INGRESAR DE NUEVO
while cant_alumnos <=0:
    print('Número no válido, inténtelo de nuevo')
    cant_alumnos = int(input('Ingrese la cantidad de alumnos: \n'))

else:
    print(f'La cantidad de alumnos es : {cant_alumnos}')

#GUARDAR EL NOMBRE DE ASIGNATURA
asignatura = str(input('Ingrese el nombre de la asignatura: \n'))

nombres = []
notas = []

nombre = input('Ingrese el nombre del primer alumno \n')
nombres.append(nombre)


for i in range(1, cant_alumnos):
        nombre = input('Ingrese nombre del siguiente alumno: \n')
        nombres.append(nombre)


