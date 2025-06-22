"""Camilo y Karla"""

#el resultado
Suma = 0

valor1 = 500 
#se suman de 10 en 10

valor2 = 456  
#se restan de 2 en 2


# Bucle para calcular la sumatoria.

while valor1 <= 800 and valor2 >= 0:
    Suma += valor1 + valor2
    valor1 += 10
    valor2 -= 2
# Mostrar el resultado
print(f"La sumatoria del patron s = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800 es : {Suma}")