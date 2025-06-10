
from colorama import init, Fore #FUNCIÓN 'FORE' EXTRAE LOS COLORES
init()

#CONDICIONAL IF
print(Fore.CYAN + '############ 01 - UTILIZANDO IF Y ELSE#########')

licencia = False
edad = 19
automovil = False

#¿ESTARÁ CORRECTO ESTE CÓDIGO?
#Incorrecto

print(Fore.YELLOW + '\n>>>Testeando los comparadores y el IF')
if licencia and edad>= 18:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia.')
elif automovil:
    print(Fore.WHITE + 'Tengo automóvil, pero no la edad ni la licencia.')
else:
    print(Fore.WHITE + 'No puedo conducir porque no tengo ni la edad, ni la licencia, ni automóvil.')



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


              