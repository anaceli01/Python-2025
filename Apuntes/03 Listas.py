
#LISTA COMPUESTA DE DATOS
lista1 = ['Victor', 31, True]

print(lista1)

#LISTA VACÍA
frutas = []

#LISTA DE SOLO NÚMEROS
n = [1, 2, 3, 4, 5]

#LISTA DE SOLO STRINGS - UTILIZANDO LA FUNCIÓN LIST
ramos = ['Programación', 'Química', 'POO']

print(ramos[0]) #imprime la posición del primer elemento de la lista (No el carácter)

#MÉTODO COUNT (CUENTA LA CANTIDAD DE CONCURRENCIA DE UN ELEMENTO)
print(ramos.count('Programación'))

#MÉTODO APPEND (AGREGANDO UN ELEMENTO AL FINAL DE LA LISTA)
ramos.append('Introducción a la Matemática')
print(ramos)

#MODIFICAR ELEMENTOS A LA LISTA
ramos[1] = 'Comunicación' #estoy pasando la posición del elemento a modificar
print(ramos)

#OTRA FORMA DE INSERTAR UN ELEMENTO A LA LISTA (INSERT)
ramos.insert(0,'Algebra') #inserta un elemento 'Algebra', en la primera Posición (0)
print(ramos)

#ELIMINAR EL ÚLTIMO ELEMENTO DE UNA LISTA
ramos.pop()
print(ramos)

#ORDENANDO ELEMENTOS DE UNA LISTA DE FORMA DESCENDENTE A ASCENDENTE
print(ramos.sort()) #no se puede hacer
ramos.sort()
print(ramos)

#ORDENANDO ELEMENTOS DE UNA LISTA SEGÚN SU CANTIDAD DE CARÁCTERES
ramos.sort(key=len) #key es una propiedad del método sort y se pasa un valor que es el método len
print(ramos)

#OCUPANDO EL MÉTODO EXTENDIDO
ramitos = ['Cálculo', 'Autómata'] #nueva lista
ramos.extend(ramitos) #agrega una lista (ramitos) a otra (ramos)
print(ramos)







