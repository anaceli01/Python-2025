"""Camilo y Karla"""

#Diccionario de los empleados

empleados = {
    'Irene' :{
        'dia_1' : 159990,
        'dia_2' : 101990,
        'dia_3' : 175990,
        'dia_4' : 225990,
        'dia_5' : 228990
    },

    'Sebastian':{
        'dia_1' : 289990,
        'dia_2' : 315990,
        'dia_3' : 237990,
        'dia_4' : 203990,
        'dia_5' : 398990
    },

    'Dante': {
        'dia_1' : 315990,
        'dia_2' : 372990,
        'dia_3' : 397990,
        'dia_4' : 411990,
        'dia_5' : 299990
    }

}

#Declaración del sueldo base
sueldo_base = 529000

#IRENE

#Variable con las ventas de Irene
ventas_i = [empleados['Irene']['dia_1'], empleados['Irene']['dia_2'], empleados['Irene']['dia_3'], empleados['Irene']['dia_4'], empleados['Irene']['dia_5']]

#Variable con el total de ventas de Irene
total_ventas_i = sum(ventas_i)

#Variable con el promedio de ventas de Irene
promedio_ventas_i = int(total_ventas_i / len(ventas_i))

#Definir bono de Irene
if total_ventas_i >= 500000 and total_ventas_i < 1000000:
    bono = sueldo_base * 0.05
elif total_ventas_i >= 1000000 and total_ventas_i < 1500000:
    bono = sueldo_base * 0.10
elif total_ventas_i >= 1500000:
    bono = sueldo_base * 0.20
else:
    bono = 0

print('Reporte de pago: \n')

#Impresión Reporte de pago de Irene
print('Irene: \n')
print(f'-Total de ventas: ${total_ventas_i}')
print(f'-Promedio de ventas: ${int(promedio_ventas_i)}')
print(f'-Bono a pagar: ${int(bono)}')
print(f'-Sueldo a pagar: ${int(sueldo_base + bono)}')




#SEBASTIAN

#Variable con las ventas de Sebastian
ventas_s = [empleados['Sebastian']['dia_1'], empleados['Sebastian']['dia_2'], empleados['Sebastian']['dia_3'], empleados['Sebastian']['dia_4'], empleados['Sebastian']['dia_5']]

#Variable con el total de ventas de Sebastian
total_ventas_s = sum(ventas_s)

#Variable con el promedio de ventas de Sebastian
promedio_ventas_s = int(total_ventas_s / len(ventas_s))

#Definir bono de Sebastian
if total_ventas_s >= 500000 and total_ventas_s < 1000000:
    bono = sueldo_base * 0.05
elif total_ventas_s >= 1000000 and total_ventas_s < 1500000:
    bono = sueldo_base * 0.10
elif total_ventas_s >= 1500000:
    bono = sueldo_base * 0.20
else:
    bono = 0

#Impresión Reporte de pago de Sebastian
print('\n')
print('Sebastian: \n')
print(f'-Total de ventas: ${total_ventas_s}')
print(f'-Promedio de ventas: ${int(promedio_ventas_s)}')
print(f'-Bono a pagar: ${int(bono)}')
print(f'-Sueldo a pagar: ${int(sueldo_base + bono)}')




#DANTE

#Variable con las ventas de Dante
ventas_d = [empleados['Dante']['dia_1'], empleados['Dante']['dia_2'], empleados['Dante']['dia_3'], empleados['Dante']['dia_4'], empleados['Dante']['dia_5']]

#Variable con el total de ventas de Dante
total_ventas_d = sum(ventas_d)

#Variable con el promedio de ventas de Dante
promedio_ventas_d = int(total_ventas_d / len(ventas_d))

#Definir bono de Dante
if total_ventas_d >= 500000 and total_ventas_d < 1000000:
    bono = sueldo_base * 0.05
elif total_ventas_d >= 1000000 and total_ventas_d < 1500000:
    bono = sueldo_base * 0.10
elif total_ventas_d >= 1500000:
    bono = sueldo_base * 0.20
else:
    bono = 0

#Impresión Reporte de pago de Dante
print('\n')
print('Dante: \n')
print(f'-Total de ventas: ${total_ventas_d}')
print(f'-Promedio de ventas: ${int(promedio_ventas_d)}')
print(f'-Bono a pagar: ${int(bono)}')
print(f'-Sueldo a pagar: ${int(sueldo_base + bono)}')