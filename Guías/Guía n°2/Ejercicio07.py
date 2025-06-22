#Ejercicio 7 - Número factorial

#Camilo y Karla

#Input del número

n = int(input('El factorial de un número es el producto de este multiplicado por los números menores e igual al número. Para saber el factorial de un número, ingrese un número entero positivo: \n'))

#Comprobando que el número sea positivo
while n < 0:
    input('No es un número positivo. Inténtelo de nuevo: \n')


#Una vez comprobado que es un entero, se pasa a calcular el factorial

#Iniciando el valor de factorial como 1
factorial = 1

#Si el número (n) es 0, el factorial es 1
if n == 0:
    print(f'El número factorial de {n} ({n}!) es: {factorial}')

#Si el número es distinto de cero, se calcula el factorial
else:
    #Hacer una lista (números), que contenga los números en el rango del número (n) a 1 (0), disminuyendo en 1 (-1)
    numeros = list(range(n, 0, -1))

    #Bucle que recorre los números en la lista y guarde la multiplicación de estos en la variable factorial
    for x in numeros:
        factorial = factorial * x
        
    print(f'El factorial del número {n} ({n}!) es : {factorial}')

       
      



