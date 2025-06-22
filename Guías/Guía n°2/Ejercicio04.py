#Ejercicio 4 - Sumar impares de n cubo

'''Camilo y Karla'''

#Ingreso por comando del número
n = int(input('Ingrese un número: \n'))

#Cálculo del cubo
cubo = n**3

#La multiplicación del número ingresado por su número antecesor da al número antecesor al primer impar
n_anterior = n * (n-1)

#Obtener el primer impar de la suma
impar_inicial = n_anterior + 1

#Lista vacía para almacenar los impares
lista = []

#Bucle for para obtener los impares
for i in range(1, n):
    impar_inicial = impar_inicial + 2
    lista.append(impar_inicial)

#Impresión de las sumas
print(f'EL cuadrado de {n} es {cubo}, por lo tanto, siguiendo la propiedad de Nicómaco de Gerasa, la suma de : {lista}, da como resultado: {cubo}')




