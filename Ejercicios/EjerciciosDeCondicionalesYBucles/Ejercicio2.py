
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
promedios = []

nota_1 = 0
nota_2 = 0
nota_3 = 0

nombre = input('Ingrese el nombre del primer alumno \n')
nombres.append(nombre)


nota_1  = float(input('Ingrese la primera nota: \n'))
nota_2 = float(input('Ingrese la segunda nota: \n'))
nota_3 = float(input('Ingrese la tercera nota: \n'))

if nota_1 <0 or nota_2 <0 or nota_3 < 0 or nota_1 >7 or nota_2 > 7 or nota_3 > 7:
     
     while nota_1 or nota_2 or nota_3 < 0 or nota_1 or nota_2 or nota_3 > 7:
        print('Una o más notas inválidas, ingreselas de nuevo: \n')
        nota_1  = float(input('Ingrese la primera nota: \n'))
        nota_2 = float(input('Ingrese la segunda nota: \n'))
        nota_3 = float(input('Ingrese la tercera nota: \n'))

else:
     promedio = (nota_1 + nota_2 + nota_3) / 3
     promedios.append(promedio)
     print(promedio)
         

for i in range(1, cant_alumnos):
    nombre = input('Ingrese nombre del siguiente alumno: \n')
    nombres.append(nombre)
    
    nota_1  = float(input('Ingrese la primera nota: \n'))
    nota_2 = float(input('Ingrese la segunda nota: \n'))
    nota_3 = float(input('Ingrese la tercera nota: \n'))

    
    if nota_1 <0 or nota_2 <0 or nota_3 < 0 or nota_1 >7 or nota_2 > 7 or nota_3 > 7:
     
            while nota_1 or nota_2 or nota_3 < 0 or nota_1 or nota_2 or nota_3 > 7:
                print('Una o más notas inválidas, ingreselas de nuevo: \n')
                for i in range(0, 3):
                    nota_1  = float(input('Ingrese la primera nota: \n'))
                    nota_2 = float(input('Ingrese la segunda nota: \n'))
                    nota_3 = float(input('Ingrese la tercera nota: \n'))

    else:
        promedio = (nota_1 + nota_2 + nota_3) / 3
        promedios.append(promedio)

estudiantes = dict(zip(nombres, promedios))
print(estudiantes)

#Estudiante con promedio más alto:
mayor = max(estudiantes)
menor = min(estudiantes)

print(f'El estudiante con el mayor promedio es : {mayor} y el estudianye con el menor promedio es : {menor}')

categoría = dict(
     Bajo = '',
     Medio = '',
     Alto = '',
     Becado = ''
)

for i in estudiantes:
    if promedio < 4:
          categoría['Bajo'].append(i)
    elif promedio <= 6:
         categoría['Medio'].append(i)
    elif promedio > 6:
         categoría['Alto'].append(i)
    elif promedio >= 5:
         categoría['Becado'].append(i)


print(categoría)

