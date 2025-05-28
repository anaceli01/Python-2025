#CREANDO UNA TUPLA 
estudiantes = ('Samir', 'Matías', 'Héctor', 'Pia', 'Carlos')
print(estudiantes)

#CREANDO OTRA TUPLA
tuplita = ([1, 2, 3], ('Santiago', 'Viña'), {'Manzana', 'Piña'})
print(tuplita)

#ELIMINANDO EL ÚLTIMO ELEMENTO DE LA TUPLA (NO SE PUEDE -> INMUTABLE)
'''estudiantes.pop()
print(estudiantes)'''

#MÉTODO INDEX EN TUPLAS
print(estudiantes.index('Carlos')) # .index() INDICA LA POSICIÓN EN LA QUE ESTÁ 'CARLOS'

#MÉTODO SORTED EN TUPLAS
print(sorted(estudiantes)) # sorted() (ORDENA ELEMENTOS Y LO PASA A LISTA)

