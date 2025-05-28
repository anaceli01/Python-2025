#CREANDO SETS (LLeva llaves {})
colores = {'Verde', 'Rojo', 'Azul', 34}
colorcitos = {'Azul', 'Naranjo'}
print(colores)
print(colorcitos)

#AGREGANDO UN NUEVO ELEMENTO AL SET (MÉTODO ADD)
colores.add('Blanco')
print(colores)

#ELIMINANDO UN ELEMENTO DEL SET
colores.discard('Blanco')
print(colores)

#APLICANDO EL MÉTODO DIFERENCE
diferencia = colores.difference(colorcitos)
print(diferencia)
