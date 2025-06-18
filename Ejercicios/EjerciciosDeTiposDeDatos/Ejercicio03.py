#CREAR UN ALGORITMO QUE PERMITA MANIPULAR CADENAS DE TEXTO

texto = str(input('Ingrese un texto con al menos 30 carácteres: \n')) 

#IMPRIMIR EN MAYÚSCULAS
print(texto.upper())

#IMPRIMIR EN MINÚSCULAS
print(texto.lower())

#CONTAR LETRAS A
lista = texto [:30]
ocurrencia_a = lista.count('a')
ocurrencia_A = lista.count('A')

print(f'La cantidad de a repetidas es : {ocurrencia_a}')
print(f'La cantidad de A repetidas es : {ocurrencia_A}')

lista_1 = texto.split()
lista_2 = ','.join(lista_1)
print(lista_2)