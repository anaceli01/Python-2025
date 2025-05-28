#CREANDO DICCIONARIO
paciente = {
    'nombre' : 'Carlos',
    'apellido' : 'Santana',
    'edad' : 50,
    'ciudad' : 'Quellon',
    'comuna' : {'Alerce'},
    'consultas' : [14, 20, 40],
    'diagnostico' : ('resfrio'),
    'info_extra' : {
        'tipo_de_sangre' : 'A+',
        'hemograma' : 'Sin Datos'
    }
}

#IMPRESIÓN DE DICCIONARIO
print(paciente)

#OTRA FORMA DE DECLARAR UN DICCIONARIO
medico = dict(
    nombre = 'Samir',
    apellido = 'Arana',
    edad = 20,
    espcecialidad = 'Urólogo'
)

#IMPRESIÓN DE DICCIONARIOS
print(paciente)
print(medico)

#CONSULTANDO UN ELEMENTO A TRAVÉS DE LA CLAVE DEL DICCIONARIO
print(medico['nombre'])

