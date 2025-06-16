
print('1: Hamburguesa')
print('2: Pizza')
print('3: Completo')

opcion = input('Por favor, elige una opción (1-3):')

match opcion:

    case '1':
        print('Has elegido una Hamburguesa. Precio: $5.000')
    case '2':
        print('Has elegido una Pizza. Precio: $')
    case '3':
        print()


#EJEMPLO DETERMINAR ESTACIÓN SEGÚN MES
mes = 4 #abril
match mes:
    case 12 | 1 | 2:
        print('Verano')
    case 3 | 4 | 5:
        print('Otoño')


#EJEMPLO: SALUDO SEGÚN HORA DEL DÍA
hora = 18 #FORMATO 24 HORAS
match hora:
    case h if 0 <= h <6:
        print('Buenas madrugadas')
    case h if 6 <= h <12:
        print('Buenos días')
    case h if 12 <= h <18:
        print('Buenas tardes')
    case h if 18 <= h <24:
        print('Buenas noches')


#PATRONES COMPUESTOS
x = [1, 2, 3]
match x:
    case [a, b, c]: #desagrupando valores de la lista
        print(f'Elementos de la lista x: {a}, {b}, {c}')


datos = {
    'nombre' : 'Victor',
    'edad' : 31
}

match datos:
    case {'nombre': n, 'edad': e}:
        print(f'Nombre: {n}, Edad: {e}')
