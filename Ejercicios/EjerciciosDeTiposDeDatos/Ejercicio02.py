#DESARROLLAR UN ALGORTIMO CON OPERACIONES MIXTAS CON NÚMERO COMPLEJOS

num_entero = int(input('Ingrese un número entero: \n'))
num_flotante = float(input('Ingrese un número flotante: \n'))
num_complejo = complex(input('Ingrese un número complejo (ejemplo : 3+6j): \n'))


potencia_compleja = num_complejo ** num_entero
print(f'La potencia compleja es: {potencia_compleja}')

suma_mixta = num_entero + num_complejo
print(f'La suma mixta es : {suma_mixta}')

producto_mixto = num_entero * num_complejo 
print(f'El producto mixto es : {producto_mixto}')

modulo_potencia_compleja = abs(potencia_compleja)
print(f'El módulo de la potencia compleja es : {modulo_potencia_compleja: .3f}')

