#Letra a
#Diccionario

print('\n')
registro = {
    5700000 : {
    'Ciudad' : 'Castro',
    'Temperatura' : 11.8,
    'Precipitación' : 2000
    },

    5770000 : {
        'Ciudad' : 'Chonchi',
        'Temperatura' : 8.3,
        'Precipitación' : 2800
    },

    5790000 : {
        'Ciudad' : 'Quellón',
        'Temperatura' : 10.2,
        'Precipitación' : 2950
    }

}


print(f'Los registros del clima son: {registro}')
print('\n')


#Letra b
#Castro
try:
    temp = registro[5700000]['Temperatura']
    if temp <= 10:
        registro[5700000]['Clima'] = 'Frío'
    elif temp >= 10 and temp <= 15:
        registro[5700000]['Clima'] = 'Templado'
    else:
        registro[5700000]['Clima'] = 'Cálido'
        

except:
    registro[5700000]['Clima'] = 'Desconocida'

#Chonchi
try:
    temp = registro[5770000]['Temperatura']
    if temp <= 10:
        registro[5770000]['Clima'] = 'Frío'
    elif temp >= 10 and temp <= 15:
        registro[5770000]['Clima'] = 'Templado'
    else:
        registro[5770000]['Clima'] = 'Cálido'
        

except:
    registro[5770000]['Clima'] = 'Desconocida'

#Quellón
try:
    temp = registro[5790000]['Temperatura']
    if temp <= 10:
        registro[5790000]['Clima'] = 'Frío'
    elif temp >= 10 and temp <= 15:
        registro[5790000]['Clima'] = 'Templado'
    else:
        registro[5790000]['Clima'] = 'Cálido'
        

except:
    registro[5790000]['Clima'] = 'Desconocida'



print(f'El registro con el tipo de clima agregado: \n {registro}')
print('\n')


#Letra c

registro[5700000]['Meses más Lluviosos'] = []
registro[5700000]['Meses más Lluviosos'] = ['Mayo', 'Junio', 'Julio']
registro[5700000]['Meses más Lluviosos'].remove('Junio')
print(f'Registro con Meses más Lluviosos agregado a Castro: \n {registro}')
print('\n')

#Letra d
registro[5770000]['Ciudad'].replace('Chonchi', 'Ciudad de los Tres Pisos')
print(f'Registro con Chonchi reemplazado por Ciudad de los Tres Pisos: \n {registro}')
print('\n')
#Letra e

#Crear lista con las precipitaciones
lluvias = [registro[5700000]['Precipitación'], registro[5770000]['Precipitación'], registro[5790000]['Precipitación']]

#Suma de las precipitaciones
suma = sum(lluvias)
print(f'La suma de las precipitaciones es: {suma}')
print('\n')

#Buscar la precipitación mayor
mayor = max(lluvias)
print(f'La precipitación mayor es: {mayor}')
print('\n')

#Buscar la precipitación menor
menor = min(lluvias)
print(f'La precipitación menor es: {menor}')
print('\n')

#Mostrar la posición de la precipitación mayor
indice = lluvias.index(mayor)
print(indice)
print('\n')

#Letra f
#Imprimir el diccionario ya completo
print(f'EL registro completo es : \n {registro}')
print('\n')

#Letra g
#Crear una tupla con las claves y valores
Lista = tuple(registro.items())
print(f'El registro en tupla es: \n {Lista}')