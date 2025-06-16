

# WHILE: ITERACIONES NO DEFINIDAS



#01 WHILE
edad = 15
num = 0

#BUCLE INFINITO
'''while edad < 18:
    print('Eres menor de edad, no puedes manejar') #ES INFINITO PORQUE LA EDAD SIEMPRE ES 18.'''



#BUCLE INFINITO
'''while True:
        print(num)
        num += 2'''



#BUCLE FINITO


num = 0
while num <= 100:
    print(num)
    num += 2 # Esto es lo mismo que 'num = num + 2'



#WHILE Y ELSE
while num <=200:
    print(num)
    num += 2
else:
    print('Mi condición es igual o mayor a 200')
    print('Segundo bloque terminado')


#BREAK
while True:
    parametro = input('>')
    if parametro == 'salir':
        break
    else:
        print(parametro)





n = 0

while n <= 50:
    n += 1
    if n ==  40:
        continue
    print(n)



#02 FOR

for i in range(1,10): #EL ÚLTIMO NÚMERO NO LO TOMA EN CUENTA
    print(i)


for i in range(1,11,2): #El TERCER NÚMERO '2', INDICA EL INTERVALO
    print(i)


#03 FOR-ELSE

for n in range(2,10):
    for i in range(2,n):
        if n % 2 == 0:
            print(f'{n} es un número compuesto, divisible por {i}')


