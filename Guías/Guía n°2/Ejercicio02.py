
"""Camilo y Karla"""

#el resultado
total = 0

valor1 = list(range(500, 800, 10))
#se suman de 10 en 10

valor2 = 456  
#se restan de 2 en 2


# Bucle para calcular la sumatoria
while valor1 <= 800 or valor2 <= 800:
        total += valor1
        tota2 += valor2
        valor2 -= 2

# Mostrar el resultado
print(f"La sumatoria del patrón es: {total}")