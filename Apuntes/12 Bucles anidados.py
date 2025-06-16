


matriz = [
    [1, 2, 3], #Fila 0
    [4, 5, 6], #Fila 1
    [7, 8, 9]  #Fila 3
  # c1 c2 c2
]

for fila_id, fila in enumerate(matriz):
    for col_id, valor in enumerate(fila):
        print(f'Posición: ({fila_id}, {col_id})= {valor}')