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
print(estudiantes.index('Carlos')) # .index() indica la posición en la que está 'Carlos'

#MÉTODO SORTED EN TUPLAS
print(sorted(estudiantes)) # sorted() (ordena elementos y lo pasa a lista)

