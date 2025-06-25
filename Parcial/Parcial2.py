
#Letra a

#Diccionario
registro = {
    101: {
        'Nombre' : 'Luna',
        'Peso' : 1.2,
        'Edad' : 3,
        'Tamaño' : 30
    },

    102: {
        'Nombre': 'Michi',
        'Peso' : 0.8,
        'Edad' : 2,
        'Tamaño' : 25
    },

    103: {
        'Nombre':'Pepito',
        'Peso' : 2.5,
        'Edad' : 5,
        'Tamaño' : 35
    }
}

#Impresión diccionario
print(f'Registro de ingresos: {registro}')

#Letra b

registro[101]['Clasificación-Peso'] = []
registro[102]['Clasificación-Peso'] = []
registro[103]['Clasificación-Peso'] = []

for i in registro.keys():
    
        if registro.values('Peso') < 1:
                registro.keys('Clasificación-Peso') = 'Bajo Peso'
        elif registro.values('Peso') >= 1 and registro.values('Peso') <= 4:
                registro.keys('Clasificación-Peso') = 'Normal'
        else:
                registro.keys('Clasificación-Peso') = 'Sobrepeso' 

print(f'Registro: \n {registro}')



#Letra c



#Letra d

lista_1 = registro[101], registro[102], registro[103]
lista_2 = registro[101]['Peso'], registro[102]['Peso'], registro[103]['Peso']
lista_3 = tuple(lista_1, lista_2)

#Letra e


nuevo = input('Ingrese un nuevo gatito: \n')

Nombre = input('Ingrese el nombre del gatito: \n')
Peso = input('Ingrese el peso del gatito: \n')
Edad = input('Ingrese la edad del gatito: \n')
Tamaño = input('Ingrese el tamaño del gatito: \n')

nuevo_registro = list(Nombre, Peso, Edad, Tamaño)
registro.udate(nuevo_registro)

respuesta = input('¿Desea agregar otro gatito?: Sí:1  No:2 \n')

while respuesta == 1:
    Nombre = input('Ingrese el nombre del gatito: \n')
    Peso = input('Ingrese el peso del gatito: \n')
    Edad = input('Ingrese la edad del gatito: \n')
    Tamaño = input('Ingrese el tamaño del gatito: \n')

    nuevo_registro = list(Nombre, Peso, Edad, Tamaño)
    registro.update(nuevo_registro)

    respuesta = input('¿Desea agregar otro gatito?: Sí:1  No:2 \n')

else:
    print('Ingresados correctamente')
        

#Letra f

respuesta = input('Para cambiar el tamaño de un gatito, ingrese el número de registro')


#Letra g


lista_peso = registro[101]['Peso'], registro[102]['Peso'], registro[103]['Peso']

promedio_pesos = sum(lista_peso) / len(lista_peso)
peso_max = max(lista_peso) 
peso_min = min(lista_peso)

print(f'Promedio de pesos: {promedio_pesos}')
print(f'Peso máximo: {peso_max}')
print(f'Peso mínimo: {peso_min}')





    