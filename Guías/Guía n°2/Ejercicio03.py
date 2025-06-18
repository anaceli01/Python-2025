

#Declaración del sueldo base
sueldo_base = 529000

#Diccionario vendedor 1
Irene = dict(
    dia_1_i = (89900, 55990, 27990, 35990),
    dia_2_i = (25990, 54990, 77990, 43990),
    dia_3_i = (47990, 56990, 35990, 27990, 46990),
    dia_4_i = (35990, 31990, 30990),
    dia_5_i = (35990, 33990, 71990, 97990)
)

#Suma de los valores en cada lista de vendedor 1
tot_d_1_i = sum(Irene['dia_1_i'])
tot_d_2_i = sum(Irene['dia_2_i'])
tot_d_3_i = sum(Irene['dia_3_i'])
tot_d_4_i = sum(Irene['dia_4_i'])
tot_d_5_i = sum(Irene['dia_5_i'])

#Suma de los totales de cada lista de vendedor 1
total_ventas_i = tot_d_1_i + tot_d_2_i + tot_d_3_i + tot_d_4_i + tot_d_5_i

#Promedio de ventas de vendedor 1
promedio_ventas_i = total_ventas_i / 5

#Bono de vendedor 1
bono_i = sueldo_base * 0.05



#Diccionario vendedor 2
Sebastian = dict(
    dia_1_s = (67990, 31990, 23990, 57990, 56990),
    dia_2_s = (32990, 42990, 79990, 31990, 59990),
    dia_3_s = (58990, 23990, 36990, 83990, 99990),
    dia_4_s = (70990, 24990, 24990, 26990, 47990),
    dia_5_s = (79990, 47990, 55990, 34990, 43990, 55990, 63990, 155990)
)

#Suma de los valores en cada lista de vendedor 2
tot_d_1_s = sum(Sebastian['dia_1_s'])
tot_d_2_s = sum(Sebastian['dia_2_s'])
tot_d_3_s = sum(Sebastian['dia_3_s'])
tot_d_4_s = sum(Sebastian['dia_4_s'])
tot_d_5_s = sum(Sebastian['dia_5_s'])

#Suma de los totales de cada lista de vendedor 2
total_ventas_s = tot_d_1_s + tot_d_2_s + tot_d_3_s + tot_d_4_s + tot_d_5_s

#Promedio de ventas de vendedor 2
promedio_ventas_s = total_ventas_s / 5

#Bono de vendedor 2
bono_s = sueldo_base * 0.20



#Diccionario vendedor 3
Dante = dict(
    dia_1_d = (20990, 55990, 23990, 119990, 88990),
    dia_2_d = (45990, 99990, 91990, 35990, 47990),
    dia_3_d = (51990, 18990, 27990, 34990, 33990),
    dia_4_d = (27990, 139990, 23990, 25990, 33990),
    dia_5_d = (22990, 12990, 8990, 35990, 67990, 29990)
)

#Suma de los valores en cada lista de vendedor 3
tot_d_1_d = sum(Dante['dia_1_d'])
tot_d_2_d = sum(Dante['dia_2_d'])
tot_d_3_d = sum(Dante['dia_3_d'])
tot_d_4_d = sum(Dante['dia_4_d'])
tot_d_5_d = sum(Dante['dia_5_d'])

#Suma de los totales de cada lista de vendedor 3
total_ventas_d = tot_d_1_d + tot_d_2_d + tot_d_3_d + tot_d_4_d + tot_d_5_d

#Promedio de vendedor 3
promedio_ventas_d = total_ventas_d / 5

#Bono de vendedor 3
bono_d = sueldo_base * 0.10


print(f'Reporte de pago: \n \n Irene: \n Total de ventas: ${total_ventas_i} \n Promedio de ventas: ${int(promedio_ventas_i)} \n Bono: ${int(bono_i)} \n Sueldo imponible: ${int(sueldo_base + bono_i)} \n \n Sebastian: \n Total de ventas: ${total_ventas_s} \n Promedio de ventas: ${int(promedio_ventas_s)} \n Bono: ${int(bono_s)} \n Sueldo imponible: ${int(sueldo_base + bono_s)} \n \n Dante: \n Total de ventas: ${total_ventas_d} \n Promedio de ventas: ${int(promedio_ventas_d)} \n Bono: ${int(bono_d)} \n Sueldo imponible: ${int(sueldo_base + bono_d)}')



