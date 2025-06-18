num = list(range(500, 99, -3))

for n in num:
    print(n)

suma = sum(num)
promedio = suma / len(num)

print(f'La suma de los número es: {suma}')
print(f'El promedio de los números es: {promedio}')